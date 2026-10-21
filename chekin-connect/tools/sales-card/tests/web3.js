const {chromium}=require("playwright-core");
const F="file://__APP__/index.html";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
const cors={"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"GET,POST,PUT,PATCH,DELETE,OPTIONS","content-type":"application/json"};
const U={"carlos@x.com":{id:"u-carlos",password:"A",role:"admin",slug:null,name:"Carlos"},"valery@x.com":{id:"u-val",password:"A",role:"admin",slug:null,name:"Valery"},"marta@x.com":{id:"u-marta",password:"A",role:"ae",slug:"marta",name:"Marta Cunha"}};
const byId=id=>Object.values(U).find(u=>u.id===id);
const S={events:[],log:[],leads:[]};
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
  if(path==="/rest/v1/leads")return j(route,200,S.leads);
  if(path==="/rest/v1/activity")return j(route,200,[]);
  if(path==="/rest/v1/events"){if(!us||us.role!=="admin")return j(route,m==="GET"?200:403,m==="GET"?[]:{message:"RLS"});
    if(m==="GET")return j(route,200,S.events);
    if(m==="POST"){body.forEach(r=>{const i=S.events.findIndex(x=>x.id===r.id);if(i>=0)S.events[i]={...S.events[i],...r};else S.events.push({created_at:"x",...r})});return j(route,201)}
    if(m==="DELETE"){const id=u.searchParams.get("id").replace("eq.","");S.events=S.events.filter(x=>x.id!==id);return j(route,204)}}
  if(path==="/rest/v1/rpc/current_event"){const t=new Date().toISOString().slice(0,10);
    const e=S.events.find(e=>!e.archived&&(e.reps||[]).includes(body.p_slug)&&(e.auto?(e.date_from<=t&&t<=(e.date_to||e.date_from)):e.active));
    return j(route,200,e?[{id:e.id,name:e.name,city:e.city,loc:e.loc}]:[])}
  return j(route,404,{message:"no route "+path})};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const pg=async(w=430)=>{const c=await b.newContext({viewport:{width:w,height:900},locale:"es-ES"});await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",S.handle);await c.addInitScript(()=>{window._opened=[]});const p=await c.newPage();p.errs=[];p.on("pageerror",e=>p.errs.push(e.message));return p};
const login=async(p,e)=>{await p.fill("#meE",e);await p.fill("#meP","A");await p.click("#meGo");await p.waitForTimeout(700)};

const D=(n,k,f,t,r,id)=>({id:id||n,name:n,kind:k,date_from:f,date_to:t||f,time_txt:"",loc:"",city:"",auto:true,days_before:k==="webinar"?0:1,active:false,archived:false,reps:r||[],created_at:n});
S.events=[D("Scale Fest","event","2026-10-24","2026-10-25",["pablo"]),D("AIGAB","event","2026-10-26","2026-10-27",["giulia"]),D("Avaibook España","webinar","2026-10-29",null,["manuel"]),D("avvapro ES (Verifactu)","webinar",null,null,["giulia"])];
S.events[3].date_from=null;S.events[3].date_to=null;
const mk=(e,ch,pr,n)=>Array.from({length:n},(_,i)=>({event_name:e,channel:ch(i),properties:pr(i),ae_id:"u-marta",ae_slug:"marta",id:e+i,created_at:"2026-10-20T10:00:00Z",first_name:"a",last_name:"b",phone:"1",email:"e@e.com"}));
S.leads=[...mk("Scale Fest",i=>i%2?"demo":"whatsapp",i=>20,10),...mk("AIGAB",i=>i%10===0?"demo":"email",i=>3,10),...mk("Avaibook España",i=>i%2?"demo":"email",i=>12,8)];
const A=await pg(393);await A.goto(F);await login(A,"carlos@x.com");
ok(await A.locator("[data-tab]").count()===5,"hay 5 pestañas (con Webinars)");
await A.screenshot({path:SH+"panel-pestanas.png"});
await A.click('[data-tab="events"]');await A.waitForTimeout(900);
let tx=await A.textContent("#tabBody");
ok(/Scale Fest/.test(tx)&&/AIGAB/.test(tx)&&!/Avaibook España/.test(tx.replace(/Calidad[\s\S]*?Total/,"")),"Eventos: solo eventos presenciales");
ok(/Leads/.test(tx),"sale la tabla de leads de eventos");
ok(!/Revisar|Calidad/.test(await A.locator("#qual").textContent())&&/Leads/.test(await A.locator("#qual").textContent()),"la tabla se titula «Leads» y no juzga la calidad");
await A.screenshot({path:SH+"panel-eventos-calidad.png",fullPage:true});
await A.click('[data-tab="webinars"]');await A.waitForTimeout(500);
tx=await A.textContent("#tabBody");
ok(/Avaibook España/.test(tx)&&/Verifactu/.test(tx)&&!/Scale Fest/.test(tx.replace(/Calidad[\s\S]*?Total/,"")),"Webinars: solo webinars");
ok(/Añadir webinar/.test(tx),"botón «+ Añadir webinar»");
await A.click("#addEv");await A.waitForSelector("#vName");
ok(await A.locator("#vCity").getAttribute("type")==="hidden"&&/Nuevo webinar/.test(await A.textContent(".sheet")),"el editor de webinar no pide ciudad");
await A.fill("#vName","Webinar nuevo");await A.fill("#vFrom","2026-12-01");await A.click("#vSave");await A.waitForTimeout(500);
const nw=S.events.find(e=>e.name==="Webinar nuevo");ok(nw&&nw.kind==="webinar"&&nw.days_before===0,"el webinar nuevo se guarda con kind=webinar y 0 días antes");
// actividad: filtro por tipo
await A.click('[data-tab="act"]');await A.waitForTimeout(500);
ok(await A.locator('#lf option[value="kind:webinar"]').count()===1,"actividad: filtro «Todos los webinars»");
ok(!(A.errs||[]).length,"sin errores JS "+JSON.stringify(A.errs));
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
