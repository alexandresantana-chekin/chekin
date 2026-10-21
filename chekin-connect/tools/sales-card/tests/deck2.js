const {chromium}=require("playwright-core");
const F="file://__APP__/index.html";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const c=await b.newContext({viewport:{width:393,height:800},locale:"es-ES"});const sent=[];
await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",r=>{const u=r.request().url();if(u.includes("submit_lead")){sent.push(JSON.parse(r.request().postData()));return r.fulfill({status:200,headers:{"access-control-allow-origin":"*","content-type":"application/json"},body:'"x"'})}
 if(r.request().method()==="OPTIONS")return r.fulfill({status:204,headers:{"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"*"}});r.abort()});
const p=await c.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));
await p.goto(F+"?c=marta&d="+Buffer.from(JSON.stringify({n:"Marta Cunha",p:"+34 611 000 000",m:"m@chekin.com"})).toString("base64url"));await p.waitForTimeout(600);
await p.click("#deckBtn");await p.waitForTimeout(200);
await p.evaluate(()=>document.querySelector(".solcard").addEventListener("click",e=>e.preventDefault()));
await p.click(".solcard");await p.evaluate(()=>{document.querySelector(".modal").remove()});
await p.evaluate(()=>document.dispatchEvent(new Event("visibilitychange")));await p.waitForTimeout(900);
ok(await p.locator("#lfK").count()===1,"al volver de la presentación sin datos captados, pide los datos");
await p.screenshot({path:SH+"deck-lead.png"});
await p.fill('#lfK [name=first]',"Ana");await p.fill('#lfK [name=last]',"Prueba");await p.fill('#lfK [name=phone]',"+34 600 111 222");await p.fill('#lfK [name=email]',"ana@e.com");await p.fill('#lfK [name=props]',"12");await p.check('#lfK [name=consent]');
await p.click("#lfSend");await p.waitForTimeout(500);
ok(sent.length===1&&sent[0].p_slug==="marta"&&sent[0].p_first==="Ana"&&sent[0].p_consent===true,"lead enviado: "+JSON.stringify(sent[0]&&{s:sent[0].p_slug,c:sent[0].p_channel}));
// segunda vez: ya captado, no vuelve a pedir
await p.click("#deckBtn");await p.evaluate(()=>document.querySelector(".solcard").addEventListener("click",e=>e.preventDefault()));await p.click(".solcard");await p.evaluate(()=>document.querySelector(".modal").remove());
await p.evaluate(()=>document.dispatchEvent(new Event("visibilitychange")));await p.waitForTimeout(900);
ok(await p.locator("#lfK").count()===0,"si ya dejó sus datos, no se los vuelve a pedir");
ok(!errs.length,"sin errores "+errs);
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
