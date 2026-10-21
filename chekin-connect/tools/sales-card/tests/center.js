const {chromium}=require("playwright-core");
const B="file://__APP__/";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const d=Buffer.from(JSON.stringify({n:"Giulia",p:"+34 603 188 291",m:"g@chekin.com"})).toString("base64url");
for(const [loc,w,h,n] of [["es-ES",393,760,"es"],["en-GB",360,640,"en"],["it-IT",393,760,"it"]]){
 const c=await b.newContext({viewport:{width:w,height:h},locale:loc});await c.route("**/*.supabase.co/**",r=>r.abort());const p=await c.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));
 await p.goto(B+"index.html?c=giulia&d="+d);await p.waitForTimeout(600);await p.click("#deckBtn");await p.waitForTimeout(300);
 const sh=await p.locator(".modal.center .sheet").boundingBox();
 const mid=sh.y+sh.height/2;ok(Math.abs(mid-h/2)<h*0.12,n+": desplegable centrado (centro y="+Math.round(mid)+" de "+h+")");
 ok(await p.locator(".solcard").count()===5&&await p.locator(".solcard.off").count()===2&&await p.locator("a.solcard").count()===3,n+": 5 tipos, 3 con presentación (apartamentos, villas, hoteles) y 2 próximamente");
 ok(sh.y>=0&&sh.y+sh.height<=h,n+": cabe en pantalla");
 await p.screenshot({path:SH+"deck-picker-"+n+".png"});ok(!errs.length,n+": sin errores "+errs);await c.close()}
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
