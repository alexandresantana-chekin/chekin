const {chromium}=require("playwright-core");const {PNG}=require("pngjs");
const F="file://__APP__/index.html";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
/* ---------- servidor Supabase simulado ---------- */
function fake(){
  const U={
    "prueba@x.com":{id:"u-prueba",password:"Provisional-1234",role:"ae",slug:"prueba",name:"Alex (prueba)",must:true,phone:"+34 608851005",contact_email:"prueba@x.com",calendly_url:"",photo_path:""},
    "giulia@x.com":{id:"u-giulia",password:"x",role:"ae",slug:"giulia",name:"Giulia",must:false,phone:"+34 699 999 999",contact_email:"giulia@x.com",calendly_url:"https://calendly.com/giulia/demo",photo_path:"u-giulia/1.jpg"},
    "carlos@x.com":{id:"u-carlos",password:"AdminPass-12345",role:"admin",slug:null,name:"Carlos",must:false,phone:"",contact_email:"",calendly_url:"",photo_path:""}};
  const byId=id=>Object.values(U).find(u=>u.id===id);
  const leads=[{id:"l1",created_at:"2026-10-19T10:00:00Z",ae_id:"u-prueba",ae_slug:"prueba",event_name:"Scale Fest",event_city:"Barcelona",first_name:"Lead",last_name:"PRUEBA Uno",phone:"+34 600 000 001",email:"p1@e.com",properties:3,channel:"whatsapp",demo_first_at:"2026-10-20T09:00:00Z",demo_last_at:"2026-10-20T09:00:00Z",demo_clicks:1},
    {id:"l2",created_at:"2026-10-19T11:00:00Z",ae_id:"u-giulia",ae_slug:"giulia",event_name:"",event_city:"",first_name:"Lead",last_name:"DE GIULIA",phone:"+34 600 000 003",email:"p3@e.com",properties:5,channel:"email"}];
  const S={U,leads,log:[],uploads:[],deleted:[],offline:false,sessions:{}};
  const cors={"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"GET,POST,PUT,PATCH,DELETE,OPTIONS","content-type":"application/json"};
  const j=(route,status,body)=>route.fulfill({status,headers:cors,body:body===undefined?"":JSON.stringify(body)});
  const who=req=>{const a=req.headers()["authorization"]||"";const m=a.match(/^Bearer tok-(.+)$/);return m?byId(m[1]):null};
  S.handle=async route=>{
    const req=route.request(),u=new URL(req.url()),path=u.pathname,m=req.method();
    if(m==="OPTIONS")return route.fulfill({status:204,headers:cors});
    if(S.offline)return route.abort("failed");
    let body=null;try{body=req.postData()?JSON.parse(req.postData()):null}catch(e){}
    S.log.push({m,path,q:u.search,body});
    if(path==="/auth/v1/token"){
      if(u.searchParams.get("grant_type")==="password"){const us=U[(body.email||"").toLowerCase()];if(!us||us.password!==body.password)return j(route,400,{error_description:"Invalid login credentials"});
        return j(route,200,{access_token:"tok-"+us.id,refresh_token:"r-"+us.id,expires_in:3600,user:{id:us.id,email:body.email}})}
      return j(route,200,{access_token:"tok-"+body.refresh_token.slice(2),refresh_token:body.refresh_token,expires_in:3600,user:{id:body.refresh_token.slice(2),email:"x"}})}
    if(path==="/auth/v1/logout")return j(route,204);
    if(path==="/auth/v1/user"&&m==="PUT"){const us=who(req);if(!us)return j(route,401,{msg:"no"});if(body.password===us.password)return j(route,422,{msg:"New password should be different from the old password."});us.password=body.password;return j(route,200,{id:us.id})}
    if(path==="/rest/v1/rpc/mark_password_changed"){const us=who(req);if(!us)return j(route,401,{message:"JWT"});us.must=false;return j(route,204)}
    if(path==="/rest/v1/rpc/submit_lead"){
      if(body.p_consent!==true)return j(route,400,{message:"consent_required"});
      const ae=Object.values(U).find(x=>x.slug===body.p_slug);if(!ae)return j(route,400,{message:"unknown_ae"});
      leads.unshift({id:"l"+(leads.length+1),created_at:new Date().toISOString(),ae_id:ae.id,ae_slug:ae.slug,event_name:body.p_event_name,event_city:body.p_event_city,first_name:body.p_first,last_name:body.p_last,phone:body.p_phone,email:body.p_email,properties:body.p_properties,channel:body.p_channel,...(body.p_channel==="demo"?{demo_first_at:new Date().toISOString(),demo_last_at:new Date().toISOString(),demo_clicks:1}:{})});
      return j(route,200,"uuid-1")}
    if(path==="/rest/v1/rpc/mark_demo_request"){   /* igual que la función de la base: apunta la demo en el contacto más reciente de ese email con ese AE */
      const l=leads.find(x=>x.ae_slug===body.p_slug&&(x.email||"").toLowerCase()===(body.p_email||"").toLowerCase());
      if(l){const now=new Date().toISOString();l.demo_first_at=l.demo_first_at||now;l.demo_last_at=now;l.demo_clicks=(l.demo_clicks||0)+1}
      return j(route,204)}
    if(path==="/rest/v1/profiles"){
      const us=who(req);
      if(m==="GET"){
        const id=u.searchParams.get("id"),slug=(u.searchParams.get("slug")||"").replace("eq.",""),sel=u.searchParams.get("select")||"";
        if(slug){const a=Object.values(U).find(x=>x.slug===slug&&x.role==="ae");return j(route,200,a?[{slug:a.slug,name:a.name,title:"Account Executive",phone:a.phone,contact_email:a.contact_email,calendly_url:a.calendly_url,photo_path:a.photo_path,updated_at:"2026-10-19T09:00:00Z"}]:[])}
        if(!us)return j(route,401,{message:"JWT"});
        const rowOf=a=>({id:a.id,email:Object.keys(U).find(k=>U[k]===a),role:a.role,slug:a.slug,name:a.name,title:"Account Executive",phone:a.phone,contact_email:a.contact_email,calendly_url:a.calendly_url,photo_path:a.photo_path,active:true,must_change_password:a.must});
        if(id){const t=id.replace("eq.","");return j(route,200,(t===us.id||us.role==="admin")?[rowOf(byId(t))]:[])}
        return j(route,200,us.role==="admin"?Object.values(U).map(rowOf):[rowOf(us)])}
      if(m==="PATCH"){if(!us)return j(route,401,{message:"JWT"});const t=u.searchParams.get("id").replace("eq.","");if(t!==us.id)return j(route,200,[]);
        if("phone" in body)us.phone=body.phone;if("contact_email" in body)us.contact_email=body.contact_email;if("calendly_url" in body)us.calendly_url=body.calendly_url;if("photo_path" in body)us.photo_path=body.photo_path;
        return j(route,200,[{id:us.id,email:"x",role:us.role,slug:us.slug,name:us.name,title:"Account Executive",phone:us.phone,contact_email:us.contact_email,calendly_url:us.calendly_url,photo_path:us.photo_path,active:true,must_change_password:us.must,updated_at:"2026-10-19T12:00:00Z"}])}}
    if(path==="/rest/v1/leads"){const us=who(req);if(!us)return j(route,401,{message:"JWT"});return j(route,200,us.role==="admin"?leads:leads.filter(l=>l.ae_id===us.id))}
    if(path.startsWith("/storage/v1/object/avatars/")){const us=who(req);if(!us)return j(route,401,{message:"no"});const rel=path.replace("/storage/v1/object/avatars/","");
      if(!rel.startsWith(us.id+"/"))return j(route,403,{message:"RLS"});
      if(m==="POST"){S.uploads.push({rel,type:req.headers()["content-type"],size:(req.postDataBuffer()||Buffer.alloc(0)).length});return j(route,200,{Key:rel})}
      if(m==="DELETE"){S.deleted.push(rel);return j(route,200,{})}}
    if(path.startsWith("/storage/v1/object/public/avatars/"))return route.fulfill({status:200,headers:{"access-control-allow-origin":"*","content-type":"image/png"},body:PNG.sync.write(new PNG({width:2,height:2}))});
    return j(route,404,{message:"no route "+path});
  };
  return S;
}
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
async function newPage(S,o={}){const c=await b.newContext({viewport:{width:393,height:800},locale:"es-ES",permissions:[],...o});await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",S.handle);await c.addInitScript(()=>{window._opened=[];window.open=function(u){window._opened.push(String(u));return null}});const p=await c.newPage();p.errs=[];p.on("pageerror",e=>p.errs.push(e.message));return p}

/* ================= TARJETA DEL CLIENTE ================= */
let S=fake(),p=await newPage(S);
await p.goto(F+"?c=giulia&lang=es");await p.waitForTimeout(1500);
ok((await p.textContent(".name")).includes("Giulia"),"tarjeta: carga y pide el perfil público (nombre)");
ok(await p.locator(".avatar img").count()===1&&/storage\/v1\/object\/public\/avatars\/u-giulia\/1\.jpg/.test(await p.locator(".avatar img").getAttribute("src")),"tarjeta: la foto viene del almacén de Supabase");
await p.locator(".item.primary .head").click();await p.waitForTimeout(400);
ok(await p.locator("#lfC").count()===1,"Escríbeme: sin datos guardados se muestra el formulario");
await p.click("#lfWA");await p.waitForTimeout(200);
ok((await p.textContent(".lf-err")).length>0,"formulario vacío → aviso, no envía");
ok(S.log.filter(x=>x.path.includes("submit_lead")).length===0,"nada se guarda si el formulario no es válido");
await p.fill('#lfC [name=first]',"Laura");await p.fill('#lfC [name=last]',"Gómez");await p.fill('#lfC [name=phone]',"+34 655 111 222");await p.fill('#lfC [name=email]',"laura@hotelsol.com");await p.fill('#lfC [name=props]',"3");
await p.click("#lfWA");await p.waitForTimeout(200);
ok((await p.textContent(".lf-err")).includes("consentimiento"),"sin consentimiento no se envía");
await p.check('#lfC [name=consent]');
await p.click("#lfWA");await p.waitForTimeout(500);
const wurl=decodeURIComponent((await p.evaluate(()=>window._opened)).slice(-1)[0]||"");
ok(/wa\.me\/34699999999/.test(wurl),"WhatsApp abre con el teléfono ACTUAL de la base de datos: "+wurl.slice(0,40));
ok(/soy Laura/.test(wurl)&&/3 propiedades/.test(wurl),"el mensaje lleva su nombre y 3 propiedades");
const sl=S.log.find(x=>x.path.includes("submit_lead"));
ok(sl&&sl.body.p_slug==="giulia"&&sl.body.p_first==="Laura"&&sl.body.p_properties===3&&sl.body.p_consent===true&&sl.body.p_channel==="whatsapp","el contacto se guarda con la Account Executive, 3 propiedades, consentimiento y canal");
ok(S.leads.some(l=>l.email==="laura@hotelsol.com"),"el contacto llega a la base");
ok(await p.locator("#wa").count()===1,"tras enviar, el panel muestra ya los botones personalizados (sin volver a pedir datos)");
// Agendar demo: ya hay datos → directo, con nombre y email puestos
await p.click("#lCal");await p.waitForTimeout(300);
const cu=new URL((await p.evaluate(()=>window._opened)).slice(-1)[0]);
ok(cu.host==="calendly.com"&&cu.pathname==="/giulia/demo"&&cu.searchParams.get("name")==="Laura Gómez"&&cu.searchParams.get("email")==="laura@hotelsol.com","Agendar demo → Calendly de Giulia con nombre y email ya puestos");
await p.waitForTimeout(300);
ok(S.log.some(x=>x.path.includes("mark_demo_request")&&x.body.p_slug==="giulia"&&x.body.p_email==="laura@hotelsol.com")&&!!S.leads.find(l=>l.email==="laura@hotelsol.com").demo_first_at,"Agendar demo con datos ya dejados → la petición de demo se apunta en su contacto");
ok(p.errs.length===0,"tarjeta sin errores JS "+JSON.stringify(p.errs));

// cliente nuevo: primero pulsa Agendar demo
S=fake();p=await newPage(S);await p.goto(F+"?c=giulia&lang=es");await p.waitForTimeout(1500);
await p.click("#lCal");await p.waitForTimeout(300);
ok(await p.locator(".modal #lfD").count()===1,"Agendar demo sin datos → pide los datos antes");
await p.fill('#lfD [name=first]',"Pedro");await p.fill('#lfD [name=last]',"Ruiz");await p.fill('#lfD [name=phone]',"655000111");await p.fill('#lfD [name=email]',"pedro@h.com");await p.fill('#lfD [name=props]',"12");await p.check('#lfD [name=consent]');
await p.click("#lfGoCal");await p.waitForTimeout(400);
ok(new URL((await p.evaluate(()=>window._opened)).slice(-1)[0]).searchParams.get("name")==="Pedro Ruiz"&&S.log.some(x=>x.path.includes("submit_lead")&&x.body.p_channel==="demo"),"envía el contacto (canal demo) y abre el calendario");
await p.locator(".item.primary .head").click();await p.waitForTimeout(300);
ok(await p.locator("#lfC").count()===0&&await p.locator("#wa").count()===1,"después, Escríbeme ya no vuelve a pedir datos");

// sin conexión: el contacto no se pierde
S=fake();p=await newPage(S);await p.goto(F+"?c=giulia&lang=es");await p.waitForTimeout(1500);
S.offline=true;
await p.locator(".item.primary .head").click();
await p.fill('#lfC [name=first]',"Offline");await p.fill('#lfC [name=last]',"Prueba");await p.fill('#lfC [name=phone]',"655000222");await p.fill('#lfC [name=email]',"off@h.com");await p.fill('#lfC [name=props]',"2");await p.check('#lfC [name=consent]');
await p.click("#lfWA");await p.waitForTimeout(500);
ok(await p.evaluate(()=>JSON.parse(localStorage.getItem("chekin-lead-queue")||"[]").length)===1&&S.leads.every(l=>l.email!=="off@h.com"),"sin conexión: el contacto queda en cola, no se pierde");
S.offline=false;await p.goto(F+"?c=giulia&lang=es");await p.waitForTimeout(1200);
ok(S.leads.some(l=>l.email==="off@h.com")&&await p.evaluate(()=>JSON.parse(localStorage.getItem("chekin-lead-queue")||"[]").length)===0,"al volver la conexión, se envía solo y la cola queda vacía");

/* ================= PERFIL DE CADA PERSONA ================= */
S=fake();p=await newPage(S);await p.goto(F+"?me=1&lang=es");await p.waitForTimeout(600);
ok(await p.locator("#meF").count()===1,"?me=1 sin sesión → pantalla de entrada");
await p.fill("#meE","prueba@x.com");await p.fill("#meP","mala");await p.click("#meGo");await p.waitForTimeout(400);
ok((await p.textContent("#meErr")).includes("incorrectos"),"clave mala → aviso");
await p.fill("#meP","Provisional-1234");await p.click("#meGo");await p.waitForTimeout(700);
ok((await p.textContent(".me-card h1")).includes("Elige tu contraseña"),"primer acceso → obliga a elegir contraseña");
await p.fill('[name=p1]',"corta");await p.fill('[name=p2]',"corta");await p.click(".me-pwform button");await p.waitForTimeout(200);
ok((await p.textContent(".me-pwform .me-err")).includes("10 caracteres"),"contraseña corta → aviso");
await p.fill('[name=p1]',"MiClaveNueva-2026");await p.fill('[name=p2]',"otra-distinta-123");await p.click(".me-pwform button");await p.waitForTimeout(200);
ok((await p.textContent(".me-pwform .me-err")).includes("no coinciden"),"no coinciden → aviso");
await p.fill('[name=p1]',"Provisional-1234");await p.fill('[name=p2]',"Provisional-1234");await p.click(".me-pwform button");await p.waitForTimeout(500);
ok((await p.textContent(".me-pwform .me-err")).includes("distinta"),"misma que la provisional → rechaza");
await p.fill('[name=p1]',"MiClaveNueva-2026");await p.fill('[name=p2]',"MiClaveNueva-2026");await p.click(".me-pwform button");await p.waitForTimeout(900);
ok(S.U["prueba@x.com"].password==="MiClaveNueva-2026"&&S.U["prueba@x.com"].must===false,"contraseña nueva guardada y marcada como cambiada");
ok(await p.locator("#meProf").count()===1,"después entra a su perfil");
const leadsText=await p.textContent("#meLeads");
ok(leadsText.includes("PRUEBA Uno")&&!leadsText.includes("DE GIULIA"),"ve SOLO sus contactos (no los de Giulia)");
// editar perfil
await p.fill("#mePhone","608851005");await p.fill("#meCal","calendly.com/sin-https");await p.click("#meProf button[type=submit]");await p.waitForTimeout(300);
ok((await p.textContent("#meProfErr")).includes("https://"),"Calendly sin https:// → aviso");
await p.fill("#meCal","https://calendly.com/alex-prueba");await p.click("#meProf button[type=submit]");await p.waitForTimeout(600);
ok(S.U["prueba@x.com"].phone==="+34 608851005"&&S.U["prueba@x.com"].calendly_url==="https://calendly.com/alex-prueba","guarda teléfono (añade +34 si falta) y Calendly");
// foto
const png=new PNG({width:600,height:400});for(let i=0;i<png.data.length;i+=4){png.data[i]=200;png.data[i+1]=80;png.data[i+2]=60;png.data[i+3]=255}
await p.setInputFiles("#meFile",{name:"yo.png",mimeType:"image/png",buffer:PNG.sync.write(png)});await p.waitForTimeout(1500);
ok(S.uploads.length===1&&/^u-prueba\/\d+\.jpg$/.test(S.uploads[0].rel)&&S.uploads[0].type==="image/jpeg","la foto se sube a SU carpeta, recortada y en JPEG ("+(S.uploads[0]&&S.uploads[0].size)+" bytes)");
ok(/^u-prueba\//.test(S.U["prueba@x.com"].photo_path)&&await p.locator(".me-av img").count()===1,"el perfil muestra la foto nueva");
await p.setInputFiles("#meFile",{name:"otra.png",mimeType:"image/png",buffer:PNG.sync.write(png)});await p.waitForTimeout(1500);
ok(S.deleted.length===1,"al cambiar la foto, borra la anterior");
// su tarjeta pública refleja los cambios sin tocar el QR
const q=await newPage(S);await q.goto(F+"?c=prueba&lang=es");await q.waitForTimeout(900);
ok((await q.textContent(".name")).includes("Alex (prueba)")&&await q.locator(".avatar img").count()===1,"la tarjeta pública de 'prueba' sale solo con datos de la base (sin d= en el enlace)");
await q.locator(".item.primary .head").click();
ok(await q.locator("#lfWA").count()===1&&!(await q.locator("#lfWA").getAttribute("class")).includes("off"),"…y su WhatsApp funciona con el teléfono que guardó");
// salir
await p.click("#meOut");await p.waitForTimeout(400);
ok(await p.locator("#meF").count()===1&&!await p.evaluate(()=>localStorage.getItem("chekin-sb-session")),"Salir cierra la sesión");
ok(p.errs.length===0,"perfil sin errores JS "+JSON.stringify(p.errs));

/* ================= ADMINISTRACIÓN ================= */
S=fake();p=await newPage(S,{acceptDownloads:true});await p.goto(F+"?me=1&lang=es");await p.waitForTimeout(500);
await p.fill("#meE","carlos@x.com");await p.fill("#meP","AdminPass-12345");await p.click("#meGo");await p.waitForTimeout(900);
ok((await p.textContent(".me-h1")).includes("Contactos del equipo")&&(await p.textContent("#meAdminSub")).includes("2 contactos"),"administrador: ve TODOS los contactos (2)");
const dq=await p.locator(".me-q").nth(1).textContent();
ok(dq.includes("Demos pedidas · 1")&&dq.includes("PRUEBA Uno")&&dq.includes("p1@e.com")&&dq.includes("+34 600 000 001"),"administrador: tabla «Demos pedidas» con la persona, su email y su teléfono");
ok((await p.textContent(".me-q")).includes("Sin evento"),"la tabla de Leads cuenta también los contactos sin evento");
await p.selectOption("#meFilter","u-giulia");await p.waitForTimeout(200);
ok((await p.textContent("#meAdminSub")).includes("1 contactos")&&(await p.textContent(".me-list")).includes("DE GIULIA"),"filtra por Account Executive");
await p.selectOption("#meFilter","all");
const [dl]=await Promise.all([p.waitForEvent("download"),p.click("#meCsv")]);
const csv=require("fs").readFileSync(await dl.path(),"utf8");
ok(csv.startsWith("﻿\"Fecha\"")&&csv.includes("PRUEBA Uno")&&csv.split("\r\n").length===3,"CSV con los 2 contactos (y cabecera) para Excel");
ok(csv.split("\r\n")[0].includes("Pidió demo")&&csv.includes("2026-10-20T09:00:00Z"),"el CSV lleva la fecha en que pidió la demo");
ok((await p.textContent(".me-team")).includes("Giulia")&&(await p.textContent(".me-team")).includes("Alex (prueba)"),"lista de perfiles del equipo con su estado");
ok(p.errs.length===0,"administración sin errores JS "+JSON.stringify(p.errs));

/* ================= PRESENTACIONES ================= */
S=fake();p=await newPage(S);await p.goto(F+"?c=giulia&lang=es");await p.waitForTimeout(800);
await p.click("#deckBtn");await p.waitForTimeout(300);
const hrefs=await p.$$eval("a.solcard",as=>Object.fromEntries(as.map(a=>[a.dataset.ty,a.href])));
ok(/presentaciones\/hotels-en\.html$/.test(hrefs.hotel),"Hoteles (tarjeta en español, aún sin versión ES) → presentación en inglés: "+hrefs.hotel.split("/").slice(-2).join("/"));
ok(/chekin\.com\/apartamentos\//.test(hrefs.vacation)&&/chekin\.com\/villas\//.test(hrefs.villa),"Apartamentos y villas (aún sin presentación) → su página web");
ok(/chekin\.com\/campings\//.test(hrefs.camping),"Campings → su página web");
await p.goto(F+"?c=giulia&lang=en");await p.waitForTimeout(700);await p.click("#deckBtn");
ok(/presentaciones\/hotels-en\.html$/.test(await p.locator('a[data-ty=hotel]').getAttribute("href")),"tarjeta en inglés → presentación en inglés");
console.log(`\nRESULTADO: ${pass} correctas, ${fail} fallos`);
await b.close();process.exit(fail?1:0)})();
