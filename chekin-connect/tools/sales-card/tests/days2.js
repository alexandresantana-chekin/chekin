const {chromium}=require("playwright-core");
const F="file://__APP__/index.html";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
const cors={"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"GET,POST,PUT,PATCH,DELETE,OPTIONS","content-type":"application/json"};
const U={"carlos@x.com":{id:"u-carlos",password:"A",role:"admin",slug:null,name:"Carlos"},"valery@x.com":{id:"u-val",password:"A",role:"admin",slug:null,name:"Valery"},"marta@x.com":{id:"u-marta",password:"A",role:"ae",slug:"marta",name:"Marta Cunha"}};
const byId=id=>Object.values(U).find(u=>u.id===id);
const S={events:[],log:[]};
const j=(r,st,b)=>r.fulfill({status:st,headers:cors,body:b===undefined?"":JSON.stringify(b)});
const prof=a=>({id:a.id,email:"x",role:a.role,slug:a.slug,name:a.name,title:"Account Executive",phone:"",contact_email:"",calendly_url:"",photo_path:"",active:true,must_change_password:false});
S.handle=async route=>{const req=route.request(),u=new URL(req.url()),path=u.pathname,m=req.method();
  if(m==="OPTIONS")return route.fulfill({status:204,headers:cors});
  let body=null;try{body=req.postData()?JSON.parse(req.postData()):null}catch(e){}
  const a=(req.headers().authorization||"").match(/^Bearer tok-(.+)$/),us=a?byId(a[1]):null;S.log.push(m+" "+path+u.search);
  if(path==="/auth/v1/token"){const x=U[body.email];if(!x||x.password!==body.password)return j(route,400,{error_description:"bad"});return j(route,200,{access_token:"tok-"+x.id,refresh_token:"r-"+x.id,expires_in:3600,user:{id:x.id,email:body.email}})}
  if(path==="/auth/v1/logout")return j(route,204);
  if(path==="/rest/v1/profiles"){if(!us)return j(route,401,{});
    if(u.searchParams.get("id"))return j(route,200,[prof(byId(u.searchParams.get("id").replace("eq.","")))]);
    if(u.searchParams.get("role"))return j(route,200,[{slug:"marta",name:"Marta Cunha",title:"Account Executive",phone:"+34 611 000 000",contact_email:"marta@chekin.com",calendly_url:"",photo_path:"",updated_at:"x"}]);
    if(u.searchParams.get("slug")){const s=u.searchParams.get("slug").replace("eq.","");return j(route,200,s==="marta"?[{slug:"marta",name:"Marta Cunha",title:"Account Executive",phone:"+34 611 000 000",contact_email:"marta@chekin.com",calendly_url:"",photo_path:"",updated_at:"x"}]:[])}
    return j(route,200,[])}
  if(path==="/rest/v1/leads")return j(route,200,[]);
  if(path==="/rest/v1/events"){if(!us||us.role!=="admin")return j(route,m==="GET"?200:403,m==="GET"?[]:{message:"RLS"});
    if(m==="GET")return j(route,200,S.events);
    if(m==="POST"){body.forEach(r=>{const i=S.events.findIndex(x=>x.id===r.id);if(i>=0)S.events[i]={...S.events[i],...r};else S.events.push({created_at:"x",...r})});return j(route,201)}
    if(m==="DELETE"){const id=u.searchParams.get("id").replace("eq.","");S.events=S.events.filter(x=>x.id!==id);return j(route,204)}}
  if(path==="/rest/v1/rpc/current_event"){const t=new Date().toISOString().slice(0,10);
    const e=S.events.find(e=>!e.archived&&(e.reps||[]).includes(body.p_slug)&&(e.auto?(e.date_from<=t&&t<=(e.date_to||e.date_from)):e.active));
    return j(route,200,e?[{id:e.id,name:e.name,city:e.city,loc:e.loc}]:[])}
  return j(route,404,{message:"no route "+path})};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const pg=async(w=430,today)=>{const c=await b.newContext({viewport:{width:w,height:900},locale:"es-ES"});if(today)await c.addInitScript(d=>{const R=Date;const off=new R(d).getTime()-R.now();class D extends R{constructor(...a){if(a.length)super(...a);else super(R.now()+off)}static now(){return R.now()+off}}window.Date=D},today+"T10:00:00");await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",S.handle);await c.addInitScript(()=>{window._opened=[]});const p=await c.newPage();p.errs=[];p.on("pageerror",e=>p.errs.push(e.message));return p};
const login=async(p,e)=>{await p.fill("#meE",e);await p.fill("#meP","A");await p.click("#meGo");await p.waitForTimeout(700)};

S.events=[{id:"m",name:"Mesa Madrid",date_from:"2026-10-20",date_to:"2026-10-20",time_txt:"9:00–11:00",loc:"Hospes",city:"Madrid",auto:true,days_before:1,active:false,archived:false,reps:["marta"],created_at:"x"},
 {id:"z",name:"Cero dias",date_from:"2026-10-20",date_to:"2026-10-20",time_txt:"",loc:"",city:"",auto:true,days_before:0,active:false,archived:false,reps:["marta"],created_at:"y"}];
for(const [today,expM,expZ] of [["2026-10-18","Empieza",null],["2026-10-19","Activo ahora","Empieza"],["2026-10-20","Activo ahora","Activo ahora"],["2026-10-21","Terminado","Terminado"]]){
  const A=await pg(430,today);await A.goto(F);await login(A,"carlos@x.com");await A.click('[data-tab="events"]');await A.waitForTimeout(400);
  const m=await A.locator(".rcard",{hasText:"Mesa Madrid"}).textContent(),z=await A.locator(".rcard",{hasText:"Cero dias"}).textContent();
  ok(m.includes(expM),today+": 1 día antes -> "+expM);ok(z.includes(expZ||"Empieza"),today+": mismo día -> "+(expZ||"Empieza"));
  if(today==="2026-10-19"){await A.locator(".rcard",{hasText:"Mesa Madrid"}).locator("[data-eedit]").click();await A.waitForSelector("#vBefore");
    ok(await A.inputValue("#vBefore")==="1","el editor muestra «1 día antes»");await A.selectOption("#vBefore","2");await A.click("#vSave");await A.waitForTimeout(500);
    ok(S.events.find(e=>e.id==="m").days_before===2,"se guarda days_before=2 en la base");await A.screenshot({path:"__SHOTS__/evento-antes.png"})}
  await A.context().close()}
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
