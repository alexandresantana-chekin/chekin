const {chromium}=require("playwright-core");
const B="file://__APP__/";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const c=await b.newContext({viewport:{width:393,height:800},locale:"es-ES",acceptDownloads:true});const sent=[];
await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",r=>{if(r.request().url().includes("submit_lead")){sent.push(JSON.parse(r.request().postData()));return r.fulfill({status:200,headers:{"access-control-allow-origin":"*","content-type":"application/json"},body:'"x"'})}
 if(r.request().method()==="OPTIONS")return r.fulfill({status:204,headers:{"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"*"}});r.abort()});
const p=await c.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));
const d=Buffer.from(JSON.stringify({n:"Marta Cunha",p:"+34 611 000 000",m:"m@chekin.com",c:"https://calendly.com/marta/demo"})).toString("base64url");
await p.goto(B+"index.html?c=marta&d="+d);await p.waitForTimeout(700);
// «Guardar contacto» sin datos: pide los datos antes y no descarga
let dl=false;p.on("download",()=>dl=true);
await p.click("#saveVcf");await p.waitForTimeout(400);
ok(await p.locator("#lfS").count()===1,"«Guardar contacto» pide los datos si no los dejó");
ok(!dl,"no descarga el contacto sin datos");
await p.screenshot({path:SH+"guardar-pide-datos.png"});
await p.click("#lfGoSave");await p.waitForTimeout(200);
ok((await p.textContent("#lfS .lf-err")).length>0,"con el formulario vacío muestra el error");
await p.fill('#lfS [name=first]',"Ana");await p.fill('#lfS [name=last]',"Prueba");await p.fill('#lfS [name=phone]',"+34 600 000 000");
await p.fill('#lfS [name=email]',"ana@ejemplo.com");await p.fill('#lfS [name=props]',"12");await p.check('#lfS [name=consent]');
const [f]=await Promise.all([p.waitForEvent("download"),p.click("#lfGoSave")]);await p.waitForTimeout(800);
ok(/marta-chekin\.vcf$/.test(f.suggestedFilename()),"tras dejar los datos descarga el contacto: "+f.suggestedFilename());
ok(sent.length===1&&sent[0].p_slug==="marta"&&sent[0].p_email==="ana@ejemplo.com","el contacto llega al AE (submit_lead)");
ok(await p.locator(".modal").count()===0,"se cierra la ventana");
// segunda vez: descarga directa, sin volver a pedir datos
const [f2]=await Promise.all([p.waitForEvent("download"),p.click("#saveVcf")]);await p.waitForTimeout(300);
ok(!!f2&&await p.locator("#lfS").count()===0,"la segunda vez guarda directamente");
ok(sent.length===1,"no se envía el contacto dos veces");
ok(!errs.length,"sin errores "+errs);console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
