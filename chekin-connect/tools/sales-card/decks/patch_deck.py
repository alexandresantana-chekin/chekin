import re,sys
BACK1={"en":"← Card","es":"← Tarjeta","pt":"← Cartão","fr":"← Carte","de":"← Karte"}
BACK2={"en":"Back to the card","es":"Volver a la tarjeta","pt":"Voltar ao cartão","fr":"Retour à la carte","de":"Zurück zur Karte"}
def patch(path):
    s=open(path,encoding="utf-8").read()
    def rep(o,n,c=1):
        nonlocal s
        if s.count(o)!=c: sys.exit("%s COUNT %d!=%d: %s"%(path,s.count(o),c,o[:80]))
        s=s.replace(o,n)
    # 1. estilos
    rep("</style>","[hidden]{display:none!important}.topline .logo{flex:0 0 auto}.topline .pill{flex:0 1 auto;min-width:0;white-space:nowrap}@media(max-width:420px){.topline{gap:6px}.topline .pill{padding:0 10px;font-size:12.5px;height:34px}}@media(max-width:340px){.topline .pill.solid{display:none}}\n</style>",1) if s.count("</style>")==1 else None
    if "[hidden]{display:none!important}" not in s:
        i=s.rindex("</style>");s=s[:i]+"[hidden]{display:none!important}.topline .logo{flex:0 0 auto}.topline .pill{flex:0 1 auto;min-width:0;white-space:nowrap}@media(max-width:420px){.topline{gap:6px}.topline .pill{padding:0 10px;font-size:12.5px;height:34px}}@media(max-width:340px){.topline .pill.solid{display:none}}\n"+s[i:]
    # 2. botones de vuelta (arriba y en el último slide)
    i=s.index('<a class="pill solid" data-cta="demo"')
    s=s[:i]+'<a class="pill" id="backCard" href="#" hidden><span data-t="back1">← Card</span></a>'+s[i:]
    rep('<a class="btn ghost" data-cta="trial" href="#" target="_blank" rel="noopener">','<a class="btn ghost" id="backCard2" href="#" hidden><span data-t="back2">Back to the card</span></a>\n      <a class="btn ghost" data-cta="trial" href="#" target="_blank" rel="noopener">')
    # 3. textos en los 5 idiomas (dentro de STR)
    i=s.index('var STR={');j=s.index('J={',i)
    blk=s[i:j]
    for l in BACK1:
        pat='"%s": {"demo":'%l
        if pat not in blk: sys.exit("no STR "+l)
        blk=blk.replace(pat,'"%s": {"back1": "%s", "back2": "%s", "demo":'%(l,BACK1[l],BACK2[l]),1)
    s=s[:i]+blk+s[j:]
    # 4. lógica: viene de una tarjeta (?card=...)
    rep("var LANGS=['en','es','fr','pt','de']","""/* Si la presentación se abre desde una tarjeta (?card=...), «Reservar demo» y «Volver» regresan a esa tarjeta */
  var CARD=(function(){try{var c=new URLSearchParams(location.search).get('card');if(!c)return null;var u=new URL(c,location.href);return u.origin===location.origin?u:null}catch(e){return null}})();
  function cardUrl(go){var u=new URL(CARD.href);u.searchParams.set('from','deck');if(go)u.searchParams.set('go',go);return u.toString()}
  function applyCard(){
    if(!CARD)return;
    document.querySelectorAll('[data-cta="demo"]').forEach(function(a){a.href=cardUrl('demo');a.removeAttribute('target');a.removeAttribute('rel')});
    ['backCard','backCard2'].forEach(function(id){var a=document.getElementById(id);if(a){a.href=cardUrl('');a.hidden=false}});
    var sh=document.getElementById('share'),sh2=document.getElementById('share2');if(sh)sh.hidden=true;if(sh2)sh2.hidden=true;
  }
  var LANGS=['en','es','fr','pt','de']""")
    rep("    if(cur>=0) go(cur,true);\n  }\n\n  var h=","    applyCard();\n    if(cur>=0) go(cur,true);\n  }\n\n  var h=")
    open(path,"w",encoding="utf-8").write(s)
for p in sys.argv[1:]: patch(p);print("ok",p)
