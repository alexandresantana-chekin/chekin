const {chromium}=require("playwright-core");
const B="file://__APP__/";
const SH="__SHOTS__/";
let pass=0,fail=0;const ok=(c,m)=>{c?pass++:fail++;console.log(c?"PASS":"FAIL",m)};
(async()=>{const b=await chromium.launch({executablePath:"__CHROMIUM__"});
const card=encodeURIComponent(B+"index.html?c=giulia");
for(const f of["hotels","vacation-rental"]) for(const l of["es","en","pt","fr","de"]){
 const c=await b.newContext({viewport:{width:360,height:700}});const p=await c.newPage();const errs=[];p.on("pageerror",e=>errs.push(e.message));
 await p.goto(B+"presentaciones/"+f+".html?card="+card+"#"+l);await p.waitForTimeout(700);
 const back=await p.locator("#backCard").isVisible(),txt=(await p.textContent("#backCard")).trim();
 const demo=await p.getAttribute("a.pill.solid","href");
 const w=await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]);
 const r=await p.evaluate(()=>{const q=s=>{const e=document.querySelector(s);if(!e||e.hidden||e.offsetWidth===0)return null;const r=e.getBoundingClientRect();return[Math.round(r.left),Math.round(r.right)]};return["svg.logo","#backCard","a.pill.solid",".langsel"].map(q).filter(Boolean)});
 let ov=false;const sr=[...r].sort((a,b)=>a[0]-b[0]);for(let i=1;i<sr.length;i++)if(sr[i][0]<sr[i-1][1]-0.5)ov=true;
 ok(back&&/index\.html\?c=giulia/.test(demo)&&/go=demo/.test(demo)&&!ov&&w[0]<=w[1]&&!errs.length,f+" #"+l+": «"+txt+"» demo→tarjeta, sin solapes (ancho "+w[0]+"/"+w[1]+") "+JSON.stringify(r)+(errs.length?" ERR "+errs:""));
 if(l==="de"&&f==="hotels")await p.screenshot({path:SH+"deck-nuevo-de-360.png"});
 await c.close()}
// cambiar de idioma dentro de la presentación mantiene el enlace a la tarjeta
const p=await (await b.newContext({viewport:{width:393,height:760}})).newPage();
await p.goto(B+"presentaciones/hotels.html?card="+card+"#es");await p.waitForTimeout(500);await p.click("#langBtn");await p.click('#langMenu [data-l="pt"]');await p.waitForTimeout(400);
ok(/index\.html\?c=giulia/.test(await p.getAttribute("a.pill.solid","href"))&&/Cartão/.test(await p.textContent("#backCard")),"cambiar a PT dentro de la presentación mantiene la vuelta a la tarjeta ("+(await p.textContent("#backCard")).trim()+")");
console.log(pass+" PASS / "+fail+" FAIL");await b.close()})();
