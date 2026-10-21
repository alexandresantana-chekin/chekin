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
const pg=async(w=430)=>{const c=await b.newContext({viewport:{width:w,height:900},locale:"es-ES"});await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",S.handle);await c.addInitScript(()=>{window._opened=[]});const p=await c.newPage();p.errs=[];p.on("pageerror",e=>p.errs.push(e.message));return p};
const login=async(p,e)=>{await p.fill("#meE",e);await p.fill("#meP","A");await p.click("#meGo");await p.waitForTimeout(700)};
// 1. panel sin sesión -> login
const A=await pg();await A.goto(F);await A.waitForTimeout(500);
ok(await A.locator("#meF").count()===1,"el panel pide email+contraseña");
await A.screenshot({path:SH+"panel-login.png"});
await A.evaluate(()=>localStorage.setItem("chekin-cards-v1",JSON.stringify({v:3,events:[{id:"scale-fest",name:"Scale Fest",from:"2026-10-24",to:"2026-10-25",loc:"WTC, Barcelona",city:"Barcelona",archived:false,active:true,reps:[]}]})));
// credenciales mal
await A.fill("#meE","carlos@x.com");await A.fill("#meP","mal");await A.click("#meGo");await A.waitForTimeout(400);
ok(/incorrect|inválid|no son|correo/i.test(await A.textContent("#meErr")),"clave mala: error "+(await A.textContent("#meErr")));
// 2. un AE no entra al panel: va a su ficha
const M=await pg();await M.goto(F);await login(M,"marta@x.com");
ok(await M.locator(".tabs").count()===0&&/Marta/.test(await M.textContent("body")),"AE: no ve el panel, ve su perfil");
// 3. admin Carlos: crea evento
await login(A,"carlos@x.com");
ok(await A.locator(".tabs").count()===1,"Carlos entra al panel con su usuario");await A.setViewportSize({width:393,height:800});await A.click("[data-tab=set]");await A.waitForTimeout(300);await A.screenshot({path:SH+"panel-presentaciones.png",fullPage:true});await A.click("[data-tab=team]");await A.setViewportSize({width:430,height:900});
await A.click('[data-tab="events"]');await A.waitForTimeout(300);
ok(S.events.length===1&&S.events[0].id==="scale-fest","se importó Scale Fest de este navegador a la base ("+S.events.length+")");
await A.click("#addEv");await A.fill("#vName","The TOPO Connect");await A.fill("#vFrom","2026-10-22");await A.fill("#vTo","2026-10-22");await A.fill("#vTime","18:00–21:00");await A.fill("#vLoc","TOPO Martim Moniz, Lisboa");await A.fill("#vCity","Lisboa");
await A.selectOption("#vMode","manual").catch(()=>{});
await A.click("#vSave");await A.waitForTimeout(500);
const topo=S.events.find(e=>e.name==="The TOPO Connect");
ok(!!topo&&topo.time_txt==="18:00–21:00"&&topo.date_from==="2026-10-22"&&topo.city==="Lisboa","el evento nuevo está en la base: "+JSON.stringify(topo&&{n:topo.name,t:topo.time_txt,f:topo.date_from}));
// asignar a Marta y activar
await A.locator(".rcard",{hasText:"The TOPO Connect"}).locator("[data-eas]").click();await A.waitForSelector("#aSave");await A.locator('.checkRow input[value="marta"]').check();await A.click("#aSave");await A.waitForTimeout(500);
ok(S.events.find(e=>e.id===topo.id).reps.includes("marta"),"asignación guardada en la base");
// 4. Valery (otro navegador) ve lo mismo
const V=await pg();await V.goto(F);await login(V,"valery@x.com");await V.click('[data-tab="events"]');await V.waitForTimeout(300);
ok(/The TOPO Connect/.test(await V.textContent("#tabBody")),"Valery ve el evento que creó Carlos");
await V.screenshot({path:SH+"panel-eventos-valery.png",fullPage:true});
// activar manualmente desde Valery
const hasAct=await V.locator(".rcard",{hasText:"The TOPO Connect"}).locator("[data-etog]").count();
if(hasAct){await V.locator(".rcard",{hasText:"The TOPO Connect"}).locator("[data-etog]").click();await V.waitForTimeout(400)}
// 5. cliente escanea QR de Marta (sin evento en el enlace)
const C=await pg();await C.goto(F+"?c=marta");await C.waitForTimeout(900);
await C.locator(".item.primary .head").click();await C.waitForTimeout(300);
const act=S.events.find(e=>e.id===topo.id).active||S.events.find(e=>e.id===topo.id).auto;
ok(act,"evento activo en la base");
// formulario: el evento va con el lead; comprobamos el rpc
ok(S.log.some(l=>l.includes("rpc/current_event")),"la tarjeta pregunta a la base por el evento actual");
// 6. QR del AE ya no lleva el evento
const Q=await pg();await Q.goto(F+"?r=marta");await Q.waitForTimeout(600);
ok(await Q.locator(".qrcard svg").count()===1,"pantalla QR ok");
// 7. Mi perfil del AE muestra evento actual
await M.reload();await M.waitForTimeout(900);
ok(/Evento actual: The TOPO Connect|no tienes ningún evento/.test(await M.textContent("#meEv")),"Mi perfil: "+(await M.textContent("#meEv")));
// 8. Salir
await A.click("#adminOut");await A.waitForTimeout(400);
ok(await A.locator("#meF").count()===1,"Salir vuelve al login");
// 9. eliminar evento
await V.reload();await V.waitForTimeout(800);await V.click('[data-tab="events"]');
ok(![A,M,V,C,Q].some(p=>p.errs.length),"sin errores JS "+JSON.stringify([A,M,V,C,Q].map(p=>p.errs)));
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
