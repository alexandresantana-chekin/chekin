const {chromium}=require("playwright-core");
const B="file://__APP__/";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const d=Buffer.from(JSON.stringify({n:"Giulia",p:"+34 603 188 291",m:"g@chekin.com",c:"https://calendly.com/g/demo"})).toString("base64url");
const mk=async(w,langs)=>{const c=await b.newContext({viewport:{width:w,height:760},locale:"en-GB"});await c.addInitScript(l=>{Object.defineProperty(navigator,"languages",{get:()=>l})},langs);await c.route("**/*.supabase.co/**",r=>r.abort());const p=await c.newPage();p.errs=[];p.on("pageerror",e=>p.errs.push(e.message));return p};
const exp={es:["Escríbeme","Guardar contacto"],en:["Message me","Save contact"],it:["Scrivimi","Salva il contatto"],pt:["Escreva-me","Guardar contacto"],fr:["Écrivez-moi","Enregistrer le contact"],de:["Schreiben Sie mir","Kontakt speichern"]};
for(const l of Object.keys(exp)){
  const p=await mk(360,[l+"-"+l.toUpperCase()]);await p.goto(B+"index.html?c=giulia&d="+d);await p.waitForTimeout(500);
  const txt=await p.textContent("body");ok(exp[l].every(x=>txt.includes(x)),"detección "+l+": "+exp[l].join(" / "));
  // selector desplegable
  await p.click(".langSel .ls-cur");const mb=await p.locator(".ls-menu").boundingBox();
  ok(await p.locator(".ls-menu button").count()===6&&mb.x>=0&&mb.x+mb.width<=360&&mb.y+mb.height<=760,l+": desplegable con 6 idiomas dentro de la pantalla a 360 px");
  if(l==="de")await p.screenshot({path:SH+"selector-idiomas.png"});
  // presentación
  await p.keyboard.press("Escape");await p.mouse.click(5,300);await p.waitForTimeout(150);
  await p.click("#deckBtn");const hs=await p.$$eval("a.solcard",a=>a.map(x=>x.getAttribute("href")));
  const want=l==="it"?[/hotels-it\.html\?card=/,/vacation-rental\.html\?card=.*#en/,/vacation-rental\.html\?card=.*#en/]:[new RegExp("vacation-rental\\.html\\?card=.*#"+l),new RegExp("vacation-rental\\.html\\?card=.*#"+l),new RegExp("hotels\\.html\\?card=.*#"+l)];
  ok(hs.length===3&&want.every((w,i)=>w.test(hs[i])),l+": presentaciones → "+hs.map(x=>x.replace(/\?card=[^#]*/,"?card=…").split("presentaciones/")[1]).join(" | "));
  ok(!p.errs.length,l+": sin errores "+p.errs);await p.context().close()}
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
