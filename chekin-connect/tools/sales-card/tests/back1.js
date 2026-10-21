const {chromium}=require("playwright-core");
const B="file://__APP__/";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const c=await b.newContext({viewport:{width:393,height:800},locale:"es-ES"});const sent=[];
await c.route("**/lxjefebmndcbnoxlyykw.supabase.co/**",r=>{if(r.request().url().includes("submit_lead")){sent.push(JSON.parse(r.request().postData()));return r.fulfill({status:200,headers:{"access-control-allow-origin":"*","content-type":"application/json"},body:'"x"'})}
 if(r.request().method()==="OPTIONS")return r.fulfill({status:204,headers:{"access-control-allow-origin":"*","access-control-allow-headers":"*","access-control-allow-methods":"*"}});r.abort()});
const p=await c.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));
const d=Buffer.from(JSON.stringify({n:"Marta Cunha",p:"+34 611 000 000",m:"m@chekin.com",c:"https://calendly.com/marta/demo"})).toString("base64url");
await p.goto(B+"index.html?c=marta&d="+d);await p.waitForTimeout(700);
await p.click("#deckBtn");const href=await p.getAttribute('a.solcard[href*="hotels"]',"href"),tgt=await p.getAttribute('a.solcard[href*="hotels"]',"target");
ok(/hotels\.html\?card=/.test(href)&&tgt===null,"Hoteles: abre la presentación en la misma pestaña con ?card=");
await p.click('a.solcard[href*="hotels"]');await p.waitForTimeout(900);
ok(/hotels\.html/.test(p.url()),"estamos en la presentación");
ok(await p.locator("#backCard").isVisible(),"botón «← Tarjeta» visible");
await p.screenshot({path:SH+"deck-es-volver.png"});
// Reservar demo -> vuelve a la tarjeta y abre la agenda con captación
const demo=await p.getAttribute("a.pill.solid","href");ok(/index\.html\?c=marta/.test(demo)&&/go=demo/.test(demo),"«Reservar demo» apunta a la tarjeta: "+demo.slice(0,90));
await p.click("a.pill.solid");await p.waitForTimeout(3000);
ok(/\?c=marta/.test(p.url())&&!/from=deck/.test(p.url()),"vuelve a la tarjeta y limpia el enlace");
ok(await p.locator("#lfD").count()===1,"abre el formulario de datos con el botón de la agenda");
await p.screenshot({path:SH+"vuelta-demo.png"});
// Volver sin demo -> pide datos
await p.goto(B+"index.html?c=marta&d="+d);await p.waitForTimeout(500);
await p.evaluate(()=>{try{localStorage.removeItem("chekin-lead")}catch(e){}});
await p.goto(B+"presentaciones/hotels.html?card="+encodeURIComponent(B+"index.html?c=marta&d="+d));await p.waitForTimeout(800);
await p.click("#backCard");await p.waitForTimeout(3000);
ok(await p.locator("#lfK").count()===1,"«← Tarjeta» vuelve y pide los datos si no los dejó");
// tarjeta externa (otro origen) no se acepta
await p.goto(B+"presentaciones/hotels.html?card="+encodeURIComponent("https://evil.example/x"));await p.waitForTimeout(500);
ok(await p.locator("#backCard").isHidden(),"un ?card= de otra web no se acepta");
ok(!errs.length,"sin errores "+errs);console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
