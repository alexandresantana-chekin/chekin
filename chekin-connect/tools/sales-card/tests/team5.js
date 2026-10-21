const {chromium}=require("playwright-core");
const F="file://__APP__/index.html";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
const cors={"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"GET,POST,PUT,PATCH,DELETE,OPTIONS","content-type":"application/json"};
const U={"carlos@x.com":{id:"u-carlos",password:"A",role:"admin",slug:null,name:"Carlos"},"valery@x.com":{id:"u-val",password:"A",role:"admin",slug:null,name:"Valery"},"marta@x.com":{id:"u-marta",password:"A",role:"ae",slug:"marta",name:"Marta Cunha"}};
const byId=id=>Object.values(U).find(u=>u.id===id);
const S={events:[],log:[],act:[],patch:[],tracked:[]};
const AEP=[{id:"u-marta",email:"marta@x.com",role:"ae",slug:"marta",name:"Marta Cunha",title:"Account Executive",phone:"",contact_email:"marta@x.com",calendly_url:"",photo_path:"",active:true,must_change_password:true,updated_at:"x"},{id:"u-giulia",email:"giulia@x.com",role:"ae",slug:"giulia",name:"Giulia",title:"Account Executive",phone:"+34 603 188 291",contact_email:"giulia@x.com",calendly_url:"https://calendly.com/g/d",photo_path:"",active:true,must_change_password:false,updated_at:"x"}];
const j=(r,st,b)=>r.fulfill({status:st,headers:cors,body:b===undefined?"":JSON.stringify(b)});
const prof=a=>({id:a.id,email:"x",role:a.role,slug:a.slug,name:a.name,title:"Account Executive",phone:"",contact_email:"",calendly_url:"",photo_path:"",active:true,must_change_password:false});
S.handle=async route=>{const req=route.request(),u=new URL(req.url()),path=u.pathname,m=req.method();
  if(m==="OPTIONS")return route.fulfill({status:204,headers:cors});
  let body=null;try{body=req.postData()?JSON.parse(req.postData()):null}catch(e){}
  const a=(req.headers().authorization||"").match(/^Bearer tok-(.+)$/),us=a?byId(a[1]):null;S.log.push(m+" "+path+u.search);
  if(path==="/auth/v1/token"){const x=U[body.email];if(!x||x.password!==body.password)return j(route,400,{error_description:"bad"});return j(route,200,{access_token:"tok-"+x.id,refresh_token:"r-"+x.id,expires_in:3600,user:{id:x.id,email:body.email}})}
  if(path==="/auth/v1/logout")return j(route,204);
  if(path==="/rest/v1/profiles"){if(!us)return j(route,401,{});
    if(m==="GET"&&u.searchParams.get("id"))return j(route,200,[prof(byId(u.searchParams.get("id").replace("eq.","")))]);
    if(m==="PATCH"){const id=u.searchParams.get("id").replace("eq.","");const a=AEP.find(x=>x.id===id);if(!a||us.role!=="admin")return j(route,200,[]);S.patch.push(body);Object.assign(a,body);return j(route,200,[a])}
    if(u.searchParams.get("role"))return j(route,200,AEP);
    if(u.searchParams.get("slug")){const s=u.searchParams.get("slug").replace("eq.","");return j(route,200,s==="marta"?[{slug:"marta",name:"Marta Cunha",title:"Account Executive",phone:"+34 611 000 000",contact_email:"marta@chekin.com",calendly_url:"",photo_path:"",updated_at:"x"}]:[])}
    return j(route,200,[])}
  if(path==="/rest/v1/leads")return j(route,200,[]);
  if(path==="/rest/v1/activity"){if(!us||us.role!=="admin")return j(route,200,[]);const off=+(u.searchParams.get("offset")||0);return j(route,200,off?[]:S.act)}
  if(path==="/rest/v1/rpc/track_activity"){S.tracked.push(body);return j(route,204)}
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

const A=await pg();await A.goto(F);await A.waitForTimeout(400);
S.act=[{created_at:"2026-10-19T10:00:00Z",action:"open",ae_slug:"marta",event_id:"",extra:""},{created_at:"2026-10-19T10:01:00Z",action:"deck",ae_slug:"marta",event_id:"",extra:"hotel"},{created_at:"2026-10-19T10:02:00Z",action:"demo",ae_slug:"giulia",event_id:"",extra:""}];
await login(A,"carlos@x.com");
ok(await A.locator(".rcard").count()===2,"el equipo sale de la base: 2 AEs");
ok(await A.locator("#add").count()===0,"ya no hay botón de añadir AE");
ok(/Clave sin cambiar|Password not changed/.test(await A.locator(".rcard",{hasText:"Marta"}).textContent()),"Marta aparece con «clave sin cambiar»");
await A.locator(".rcard",{hasText:"Marta"}).locator("[data-edit]").click();await A.waitForSelector("#saveR");
await A.fill("#fPhoneR","611 000 111");await A.fill("#fCalR","https://calendly.com/marta/demo");await A.click("#saveR");await A.waitForTimeout(500);
ok(S.patch.length===1&&S.patch[0].phone.replace(/\D/g,"").endsWith("611000111")&&S.patch[0].calendly_url==="https://calendly.com/marta/demo","la edición se guarda en la base: "+JSON.stringify(S.patch[0]));
// otro admin (otro navegador) ve el cambio
const V=await pg();await V.goto(F);await login(V,"valery@x.com");
await V.locator(".rcard",{hasText:"Marta"}).locator("[data-edit]").click();await V.waitForSelector("#saveR");
ok((await V.inputValue("#fPhoneR")).replace(/\D/g,"").endsWith("611000111"),"Valery ve el teléfono nuevo de Marta");
await V.click("#cancelR");
// actividad
await A.click('[data-tab="act"]');await A.waitForTimeout(600);
const kp=await A.locator(".kpis").textContent();ok(/1/.test(kp)&&(await A.textContent("#tabBody")).includes("Marta"),"la actividad sale de la base: "+kp.replace(/\s+/g," ").slice(0,80));
await A.screenshot({path:SH+"panel-actividad.png",fullPage:true});
// la tarjeta registra actividad (cliente sin sesión)
const C=await pg();await C.goto(F+"?c=marta");await C.waitForTimeout(1200);
ok(S.tracked.some(t=>t.p_slug==="marta"&&t.p_action==="open"),"la tarjeta envía «open» a la base");
// con sesión abierta (equipo probando) no cuenta
const n=S.tracked.length;await login(await (async()=>{const x=await pg();await x.goto(F+"?me=1");return x})(),"marta@x.com");
const T=await pg();await T.goto(F+"?me=1");await login(T,"marta@x.com");await T.goto(F+"?c=marta");await T.waitForTimeout(1200);
ok(S.tracked.length===n,"con sesión de equipo abierta no se cuenta la visita");
ok(![A,V,C,T].some(p=>p.errs.length),"sin errores JS "+JSON.stringify([A,V,C,T].map(p=>p.errs)));
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
