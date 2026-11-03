import re,os
os.chdir('onb/project')
R=lambda f:open(f).read()
def _aa(s):
    import re as _re
    s=s.replace('color: #6B6B95','color: #55557F').replace('color: #9696B9','color: #6B6B95')
    s=_re.sub(r'font-size: 12px',r'font-size: 13px',s)
    s=_re.sub(r'font-size: 11px',r'font-size: 12px',s)
    s=_re.sub(r'font-size: 10px',r'font-size: 12px',s)
    return s
def W(f,s): open(f,'w').write(_aa(s))
HEAD=R('Vivienda2.dc.html').split('<div style="width: 390px',1)[0]
FOOT_m='</x-dc>'+R('Vivienda2.dc.html').split('</div>\n</x-dc>',1)[1]
FOOT_p=FOOT_m.replace('"width":390,"height":844','"width":1440,"height":900')
APPNAV=re.search(r'<nav aria-label="Menú".*?</nav>',open('../project-bak-1600/Portatil-Vivienda.dc.html').read(),re.S).group(0)
FONT="font-family: 'Proxima Nova', Montserrat, Arial, sans-serif; color: #19194B"
LOGO_M='<img src="/_blob/3ef2a56a40d5efb3f55d9f310adc6465" alt="Chekin" style="width: 86px; height: 25px">'
LOGO_W='<img src="/_blob/c25beceb5f9f805a652ba855add94f27" alt="Chekin" style="width: 104px; height: 31px">'
CAT='<svg width="24" height="16" viewBox="0 0 9 6" role="img" aria-label="Bandera de Cataluña" style="display: block; border-radius: 2px"><rect width="9" height="6" fill="#FCDD09"></rect><rect y="0.667" width="9" height="0.667" fill="#DA121A"></rect><rect y="2" width="9" height="0.667" fill="#DA121A"></rect><rect y="3.333" width="9" height="0.667" fill="#DA121A"></rect><rect y="4.667" width="9" height="0.667" fill="#DA121A"></rect></svg>'
EUS='<svg width="24" height="16" viewBox="0 0 26 18" role="img" aria-label="Bandera del País Vasco" style="display: block; border-radius: 2px"><rect width="26" height="18" fill="#D52B1E"></rect><path d="M0 0L26 18M26 0L0 18" stroke="#009B48" stroke-width="3"></path><path d="M13 0V18M0 9H26" stroke="#FFFFFF" stroke-width="3"></path></svg>'
STEPS=[('Reservas','2 min'),('Dónde están','30 s'),('Titular y viviendas','2 min'),('Parte de viajeros','3 min'),('Protección','1 min'),('Ventas extra','2 min'),('Check-in y envío','30 s')]
SH='0 1px 2px rgba(25, 25, 75, 0.06), 0 0 0 1px #ECECF5'
SHM='0 0 0 2px #385BF8, 0 12px 24px rgba(56, 91, 248, 0.14)'
def ok(t): return '<div class="stepin" style="display: flex; gap: 10px; align-items: center; padding: 10px 14px; border-radius: 12px; background: #E8F6EF; color: #0F5C3B; font-size: 14px; line-height: 1.4; font-weight: 600"><span aria-hidden="true">✓</span><span>%s</span></div>'%t
def btn(h,t,extra='',full=False): return '<a href="%s"%s class="pbtn" style="display: inline-block; %s height: 50px; line-height: 50px; padding: 0 26px; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 16px; font-weight: 700; text-align: center; text-decoration: none; box-shadow: 0 6px 16px rgba(56, 91, 248, 0.28)">%s</a>'%(h,extra,'width: 100%; box-sizing: border-box;' if full else '',t)
def errbox(msg,demo='Demo: ver el error'):
    return ('<div data-err hidden role="alert" style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 12px; border-radius: 12px; background: #FDECEC; color: #8A1F1F; font-size: 14px; line-height: 1.45; font-weight: 600"><span aria-hidden="true">!</span><span>%s</span></div>'
      '<button type="button" data-demo-err style="align-self: flex-start; padding: 6px 2px; border: 0; background: none; color: #55557F; font-size: 12px; font-weight: 600; font-family: inherit; cursor: pointer; text-decoration: underline">%s</button>')%(msg,demo)
def back(h,t='← Atrás',extra=''): return '<a href="%s"%s style="display: inline-block; height: 50px; line-height: 46px; padding: 0 22px; box-sizing: border-box; border-radius: 12px; border: 2px solid #C9CBEA; background: #FFFFFF; color: #19194B; font-size: 15px; font-weight: 700; text-decoration: none">%s</a>'%(h,extra,t)
def link(h,t,extra=''): return '<a href="%s"%s style="display: inline-block; padding: 12px 4px; font-size: 14px; font-weight: 600; color: #385BF8; text-decoration: none">%s</a>'%(h,extra,t)
def sw(on=True,label=''): return '<button type="button" role="switch" class="sw" aria-checked="%s" aria-label="%s"><span class="k"></span></button>'%('true' if on else 'false',label)
LOCK='<div style="display: flex; gap: 8px; font-size: 13px; line-height: 1.45; color: #55557F"><span aria-hidden="true">🔒</span><span>%s</span></div>'
def card(inner,pad=16,extra='',sh=SH): return '<div%s style="padding: %dpx; border-radius: 16px; background: #FFFFFF; box-shadow: %s; display: flex; flex-direction: column; gap: 10px">%s</div>'%(extra,pad,sh,inner)
def icon(e): return '<div aria-hidden="true" style="width: 52px; height: 52px; border-radius: 16px; background: linear-gradient(135deg, #EFEFFF, #E3E8FF); display: flex; align-items: center; justify-content: center; font-size: 26px">%s</div>'%e
def H(e,t,sub,small=False): return '<div class="stepin" style="display: flex; flex-direction: column; gap: 8px">%s<h1 style="margin: 4px 0 0; font-size: %dpx; line-height: 1.2; font-weight: 800; letter-spacing: -0.01em">%s</h1><p style="margin: 0; font-size: 15px; line-height: 1.5; color: #6B6B95">%s</p></div>'%(icon(e) if e else '',24 if small else 28,t,sub)
def field(i,l,ph='',t='text',hint='',extra='',val=''): return '<div style="display: flex; flex-direction: column; gap: 6px"><label for="%s" style="font-size: 14px; font-weight: 600">%s</label><input id="%s" type="%s" placeholder="%s"%s value="%s" style="height: 46px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 16px; font-family: inherit; color: #19194B; background: #FFFFFF">%s</div>'%(i,l,i,t,ph,extra,val,('<div style="font-size: 12px; line-height: 1.45; color: #6B6B95">%s</div>'%hint) if hint else '')
SAVED='<span style="font-size: 12px; color: #0F7B4F; font-weight: 600">✓ Guardado</span>'
# ---------- carcasas ----------
def rail_intro():
    tr=''.join('<div style="display: flex; gap: 10px; font-size: 14px; line-height: 1.45; color: #DCE3FF"><span style="color: #35C2A3; font-weight: 800">✓</span><span>%s</span></div>'%t for t in ['Sin tarjeta de crédito y sin permanencia.','El parte de viajeros, enviado solo y en plazo.','+200.000 propiedades y +25M de check-ins con Chekin.'])
    return ('<aside style="width: 300px; flex-shrink: 0; box-sizing: border-box; padding: 30px 26px; display: flex; flex-direction: column; gap: 26px; background: linear-gradient(180deg, #161643, #1F1F57); color: #FFFFFF">'+LOGO_W
      +'<div style="display: flex; flex-direction: column; gap: 10px"><div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: #9FB2FF">PRUEBA GRATIS 14 DÍAS</div><div style="font-size: 22px; line-height: 1.25; font-weight: 800">Cada check-in, en piloto automático</div></div>'
      +'<div style="display: flex; flex-direction: column; gap: 12px">'+tr+'</div><div style="margin-top: auto; font-size: 13px; color: #C9CBEA">Tus datos están protegidos. Cumplimos el RGPD.</div></aside>')
def rail(active,chips):
    if active==0: return rail_intro()
    items=[]
    for i,(n,t) in enumerate(STEPS,1):
        if i<active: dot='<div class="%s" style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 999px; background: #35C2A3; color: #19194B; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800">✓</div>'%('ddnew' if i==active-1 else ''); col='#C9CBEA'
        elif i==active: dot='<div style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 999px; background: #FFFFFF; color: #19194B; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800; box-shadow: 0 0 0 5px rgba(255, 255, 255, 0.16)">%d</div>'%i; col='#FFFFFF'
        else: dot='<div style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 999px; border: 1.5px solid #45458A; color: #8C8CB8; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600">%d</div>'%i; col='#8C8CB8'
        items.append('<div style="display: flex; gap: 12px; align-items: center">%s<div style="flex-grow: 1; font-size: 14px; font-weight: %s; color: %s">%s</div><div style="font-size: 12px; color: #8C8CB8">%s</div></div>'%(dot,'700' if i==active else '500',col,n,t))
    ch=''.join('<span style="padding: 5px 9px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); color: #DCE3FF; font-size: 12px">%s</span>'%c for c in chips)
    return ('<aside style="width: 300px; flex-shrink: 0; box-sizing: border-box; padding: 30px 26px; display: flex; flex-direction: column; gap: 26px; background: linear-gradient(180deg, #161643, #1F1F57); color: #FFFFFF">'+LOGO_W
      +'<div style="display: flex; flex-direction: column; gap: 16px"><div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: #9FB2FF">TU CONFIGURACIÓN · ≈ 11 MIN</div>'+''.join(items)+'</div>'
      +'<div style="margin-top: auto; display: flex; flex-direction: column; gap: 10px"><div style="font-size: 11px; font-weight: 700; letter-spacing: 0.08em; color: #8C8CB8">LO QUE NOS HAS CONTADO</div><div style="display: flex; flex-wrap: wrap; gap: 6px">%s</div>'%ch
      +'<div style="font-size: 13px; color: #C9CBEA; margin-top: 6px">¿Dudas? <a href="#" style="color: #FFFFFF; font-weight: 700">Habla con un experto</a></div></div></aside>')
def bar(active):
    pct=max(0,min(100,round(100*(active-0.5)/len(STEPS)))) if active else 0
    return '<div style="height: 4px; border-radius: 999px; background: #E6E6F2; overflow: hidden"><div class="barfill" style="height: 4px; width: %d%%; border-radius: 999px; background: linear-gradient(90deg, #385BF8, #35C2A3)"></div></div>'%pct
FOOTBAR='''<div style="flex-shrink: 0; background: #FFFFFF; box-shadow: 0 -8px 24px rgba(25, 25, 75, 0.08); padding: 16px 56px"><div style="max-width: %dpx; margin: 0 auto; display: flex; align-items: center; justify-content: %s; gap: 12px">%s<span class="obar-r" style="display: inline-flex; align-items: center; gap: 12px">%s</span></div></div>'''
def lap(title,active,chips,body,left,right,wide=False,center=False,extra=''):
    meta=('Paso %d de 7 · %s · ⏱ %s'%(active,STEPS[active-1][0],STEPS[active-1][1])) if active and active<=7 else ''
    mw=860 if wide else 640
    return HEAD.replace('Vivienda 2',title+' · portátil')+'''<div class="fx" style="position: relative; width: 1440px; height: 900px; box-sizing: border-box; display: flex; background: #F7F7FC; %s">
%s
<main style="flex-grow: 1; min-width: 0; height: 900px; display: flex; flex-direction: column">
<div style="padding: 22px 56px 0; display: flex; flex-direction: column; gap: 10px"><div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: #6B6B95"><span>%s</span>%s</div>%s</div>
<div style="flex-grow: 1; overflow-y: auto; padding: 28px 56px 32px"><div style="max-width: %dpx; margin: 0 auto; display: flex; flex-direction: column; gap: 18px">%s</div></div>
%s
</main>
%s
</div>
'''%(FONT,rail(active,chips),meta,SAVED if active else '',bar(active) if active else '',mw,body,(FOOTBAR%(mw,'center' if center else 'flex-end',left,right)) if (left or right) else '',extra)+FOOT_p
def mob(title,active,body,primary,secondary='',extra=''):
    meta=('%d/7 · %s'%(active,STEPS[active-1][0])) if active and active<=7 else ''
    return HEAD.replace('Vivienda 2',title)+'''<div style="position: relative; width: 390px; min-height: 824px; box-sizing: border-box; display: flex; flex-direction: column; background: #F7F7FC; %s">
<div style="position: sticky; top: 0; z-index: 3; background: rgba(247, 247, 252, 0.96); padding: 14px 20px 10px; display: flex; flex-direction: column; gap: 10px"><div style="display: flex; justify-content: space-between; align-items: center">%s<span style="font-size: 12px; color: #6B6B95">%s</span></div>%s</div>
<div style="flex-grow: 1; padding: 8px 20px 20px; display: flex; flex-direction: column; gap: 16px">%s</div>
%s
%s
</div>
'''%(FONT,LOGO_M,meta,bar(active) if active else '',body,('<div style="position: sticky; bottom: 0; z-index: 3; background: #FFFFFF; box-shadow: 0 -8px 24px rgba(25, 25, 75, 0.1); padding: 12px 20px 16px; display: flex; flex-direction: column; align-items: center; gap: 2px">%s%s</div>'%(primary,secondary)) if (primary or secondary) else '',extra)+FOOT_m
P=lambda n:'Portatil-%s.dc.html'%n
M=lambda n:'%s.dc.html'%n
def both(name,title,active,chips,fn,left,right,mprim,msec='',wide=False):
    W(M(name),mob(title,active,fn(M,True).replace('grid-template-columns: 1fr 1fr;','grid-template-columns: 1fr;'),mprim(M),msec(M) if msec else ''))
    W(P(name),lap(title,active,chips,fn(P,False),left(P),right(P),wide))
CH=['Alquiler vacacional','4 viviendas','España']
NX=' data-next-pms="%s" data-next-man="%s"'
# ---------- Creando (marino, ritmo Apple) ----------
mark=('<div class="crea-mark" style="width: 112px; height: 112px; border-radius: 28px; background: #19194B; display: flex; align-items: center; justify-content: center">'
  '<svg class="crea-check" width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></div>')
crea=('<div style="flex-grow: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 28px; text-align: center; padding: 40px 24px">'+mark+
  '<div aria-live="polite" style="display: flex; flex-direction: column; gap: 8px; min-height: 64px"><div class="crea-t" style="font-size: 22px; font-weight: 800">Creando tu cuenta…</div><div class="crea-s" style="font-size: 15px; color: #6B6B95">Activando tu prueba de 14 días. Sin tarjeta de crédito.</div></div>'
  '<a href="Bienvenida.dc.html" data-crea-go hidden style="display: inline-block; height: 50px; line-height: 50px; padding: 0 28px; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 16px; font-weight: 700; text-decoration: none">Continuar →</a></div>')
W(M('Creando'),HEAD.replace('Vivienda 2','Creando tu cuenta')+'<div style="width: 390px; min-height: 824px; box-sizing: border-box; display: flex; flex-direction: column; background: #FFFFFF; %s">%s</div>\n'%(FONT,crea)+FOOT_m)
W(P('Creando'),HEAD.replace('Vivienda 2','Creando tu cuenta · portátil')+'<div class="fx" style="width: 1440px; height: 900px; box-sizing: border-box; display: flex; flex-direction: column; background: #FFFFFF; %s">%s</div>\n'%(FONT,crea)+FOOT_p)
# ---------- Bienvenida (compacta) ----------
def bienv(Pp,mob_):
    rows=''.join('<div style="display: flex; gap: 12px; align-items: center; padding: 9px 0"><div style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 8px; background: #EFEFFF; color: #385BF8; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800">%d</div><div style="flex-grow: 1; font-size: 15px; font-weight: 600">%s</div><div style="font-size: 13px; color: #6B6B95">%s</div></div>'%(i,n,t) for i,(n,t) in enumerate(STEPS,1))
    return (H('👋','¡Hola, Katia! Empezamos','Lo dejamos todo configurado de una vez. En unos 11 minutos, tus huéspedes ya pueden hacer el check-in.',mob_)
      +card('<div style="display: flex; justify-content: space-between; align-items: baseline"><div style="font-size: 13px; font-weight: 700; letter-spacing: 0.06em; color: #385BF8">LO QUE VIENE</div><div style="font-size: 13px; color: #6B6B95">≈ 11 min en total</div></div>'+rows,18,' class="stepin"')
      +'<div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: #6B6B95"><span>🔒 Tus datos están protegidos. Cumplimos el RGPD.</span><span>💾 Se guarda solo: puedes seguir luego.</span></div>')
both('Bienvenida','Bienvenida',0,CH[:2],bienv,lambda Pp:link(Pp('PanelNuevo'),'Ahora no'),lambda Pp:btn(Pp('Reservas'),'Empezar →'),lambda Pp:btn(Pp('Reservas'),'Empezar →',full=True),lambda Pp:link(Pp('Panel'),'Ahora no'))
# ---------- 1 · Reservas ----------
def opt(h,ic,t,d,tm,main=False,path='man',badge=''):
    return ('<a href="%s" data-path="%s" class="stepin" style="display: flex; gap: 14px; align-items: center; padding: 16px; border-radius: 16px; background: #FFFFFF; box-shadow: %s; color: #19194B; text-decoration: none">'
      '<div aria-hidden="true" style="width: 46px; height: 46px; flex-shrink: 0; border-radius: 14px; background: #EFEFFF; display: flex; align-items: center; justify-content: center; font-size: 22px">%s</div>'
      '<div style="flex-grow: 1; display: flex; flex-direction: column; gap: 4px"><div style="font-size: 16px; font-weight: 700">%s%s</div><div style="font-size: 13px; line-height: 1.45; color: #6B6B95">%s</div></div>'
      '<div style="flex-shrink: 0; font-size: 12px; font-weight: 700; color: #0F7B4F; white-space: nowrap">⏱ %s</div></a>')%(h,path,SHM if main else SH,ic,t,badge,d,tm)
def reservas(Pp,mob_):
    fast=' <span style="margin-left: 6px; padding: 3px 7px; border-radius: 999px; background: #E8F6EF; color: #0F5C3B; font-size: 11px; font-weight: 800; vertical-align: 2px">EL MÁS RÁPIDO</span>'
    o_pms=opt(Pp('ElegirPms'),'🔗','Mi PMS o channel manager','Traemos tus viviendas y reservas: casi todo se rellena solo.','2 min',not mob_,'pms','' if mob_ else fast)
    o_cal=opt(Pp('Calendario'),'📅','Calendario de Airbnb o Booking','Pegas el enlace de cada anuncio y las reservas entran solas.','2 min',mob_,'cal',fast if mob_ else '')
    o_man=opt(Pp('Paises'),'✍️','Las llevo a mano','Para probar Chekin sin conectar nada: creas tú cada reserva.','1 min',False,'man')
    o=[o_cal,o_man,o_pms] if mob_ else [o_pms,o_cal,o_man]
    return ok('¡Empezamos, Katia! Primero, lo que más tiempo te ahorra.')+H('','¿Cómo recibes tus reservas?','Elige una. Podrás cambiarla cuando quieras.',mob_)+''.join(o)+('<div style="font-size: 13px; color: #6B6B95">El PMS se conecta mejor desde el ordenador: si lo eliges, te mandamos el enlace.</div>' if mob_ else '')
both('Reservas','Reservas',1,CH[:2],reservas,lambda Pp:'',lambda Pp:link(Pp('Paises'),'Ahora no'),lambda Pp:link(Pp('Paises'),'Ahora no'))
# ---------- 1a · Elegir PMS ----------
PMS=['Guesty','Hostaway','Lodgify','Smoobu','Avantio','Cloudbeds','Octorate','Otro']
def elegir(Pp,mob_):
    tiles=''.join('<a href="%s" data-pmsname="%s" class="stepin" style="display: block; height: 60px; line-height: 60px; border-radius: 14px; background: #FFFFFF; box-shadow: %s; color: #19194B; font-size: 16px; font-weight: 800; text-align: center; text-decoration: none">%s</a>'%(Pp('Conectar'),n if n!='Otro' else 'tu PMS',SH,n if n!='Otro' else 'Otro…') for n in PMS)
    return (H('🔗','¿Cuál es tu PMS?','Conectamos con más de 200 PMS. Elige el tuyo.',mob_)
      +'<input type="search" placeholder="🔍  Busca tu PMS" aria-label="Busca tu PMS" style="height: 48px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 16px; font-family: inherit; background: #FFFFFF">'
      +'<div style="display: grid; grid-template-columns: repeat(%d, minmax(0, 1fr)); gap: 10px">%s</div>'%(2 if mob_ else 4,tiles))
both('ElegirPms','Elige tu PMS',1,CH[:2]+['Con PMS'],elegir,lambda Pp:back(Pp('Reservas'),'← Atrás'),lambda Pp:link(Pp('Paises'),'No encuentro mi PMS'),lambda Pp:link(Pp('Paises'),'No encuentro mi PMS'))
# ---------- 1b · Conectar ----------
def conectar(Pp,mob_):
    c=card('<div style="font-size: 15px; font-weight: 700">Autoriza en <span class="pmsname">Cloudbeds</span></div><div style="font-size: 14px; line-height: 1.5; color: #6B6B95">Te llevamos a su web: entras con tu usuario de siempre y pulsas «Permitir». Vuelves aquí solo.</div>'
      '<div style="font-size: 13px; color: #0F5C3B">🔒 Nunca vemos tu contraseña.</div>'
      '<button type="button" data-oauth style="height: 50px; border: 0; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 16px; font-weight: 700; font-family: inherit; cursor: pointer">Conectar con <span class="pmsname">Cloudbeds</span> ↗</button>'
      '<div data-oauth-ok hidden style="height: 50px; line-height: 50px; border-radius: 12px; background: #0F7B4F; color: #FFFFFF; font-size: 16px; font-weight: 700; text-align: center">✓ <span class="pmsname">Cloudbeds</span> conectado</div>'+errbox('No se ha conectado: en <span class="pmsname">Cloudbeds</span> se pulsó «Cancelar». Vuelve a intentarlo o conéctalo con su API key.','Demo: permiso rechazado'),18,' class="stepin" data-errbox')
    v=('<div role="img" aria-label="Vídeo" class="stepin" style="height: 120px; border-radius: 16px; background: linear-gradient(135deg, #19194B, #2E3B9E); color: #FFFFFF; display: flex; align-items: center; gap: 14px; padding: 0 20px">'
       '<span style="width: 44px; height: 44px; flex-shrink: 0; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="#385BF8"></path></svg></span>'
       '<span><b>Cómo conectar <span class="pmsname">Cloudbeds</span></b><br><span style="font-size: 13px; color: #C9CBEA">Vídeo de 2 min</span></span></div>')
    does=('<div class="stepin" style="display: grid; grid-template-columns: %s; gap: 10px; font-size: 13px; line-height: 1.6; color: #6B6B95"><div><b style="color: #19194B">Trae de tu PMS</b><br>✓ Viviendas y reservas<br>✓ Huésped principal</div><div><b style="color: #19194B">Devuelve a tu PMS</b><br>✓ Enlace y estado del check-in<br>✓ Datos de cada huésped</div></div>')%('1fr 1fr')
    alt='<div style="font-size: 13px; color: #6B6B95">¿Tu PMS no tiene este botón? <a href="%s" style="font-weight: 700">Conéctalo con su API key, con guía y vídeo</a>.</div>'%Pp('Apikey')
    return H('','Conecta <span class="pmsname">Cloudbeds</span>','Sin copiar nada: lo apruebas en tu PMS y listo.',mob_)+c+v+does+alt
both('Conectar','Conecta tu PMS',1,CH[:2]+['Con PMS'],conectar,lambda Pp:back(Pp('ElegirPms'),'← Atrás'),lambda Pp:link(Pp('Paises'),'Ahora no')+btn(Pp('Cartera'),'Continuar →'),lambda Pp:btn(Pp('Cartera'),'Continuar →',full=True),lambda Pp:link(Pp('Paises'),'Ahora no'))
# ---------- 1c · API key ----------
def apik(Pp,mob_):
    return (H('🔑','Conéctalo con su API key','Para los PMS sin botón de autorizar. Son 3 pasos.',mob_)
      +card('<ol style="margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 6px; font-size: 15px; line-height: 1.45"><li>En tu PMS, abre <b>Ajustes</b>.</li><li>Busca <b>API</b> o <b>Integraciones</b> y copia la clave.</li><li>Pégala aquí.</li></ol>',16,' class="stepin"')
      +'<div class="stepin" style="padding: 12px 14px; border-radius: 12px; background: #EFEFFF; font-size: 14px; line-height: 1.5"><b>¿Qué es una API key?</b> Una clave que tu PMS le da a Chekin para leer tus reservas. Solo copiar y pegar.</div>'
      +'<div data-errbox style="display: flex; flex-direction: column; gap: 8px">'+field('%sak'%('m' if mob_ else 'p'),'Tu API key','Pégala aquí')+LOCK%'Se guarda cifrada y solo se usa para leer tus reservas. Puedes revocarla en tu PMS cuando quieras.'+errbox('Esta clave no funciona. Comprueba que la copiaste entera, sin espacios, o pide ayuda a un experto.','Demo: clave no válida')+'</div>')
both('Apikey','API key',1,CH[:2]+['Con PMS'],apik,lambda Pp:back(Pp('Conectar'),'← Atrás'),lambda Pp:btn(Pp('Cartera'),'Conectar y seguir →'),lambda Pp:btn(Pp('Cartera'),'Conectar y seguir →',full=True))

# ---------- 1d · Calendario de Airbnb o Booking ----------
def calendario(Pp,mob_):
    k='m' if mob_ else 'p'
    row=lambda i,ph:('<div data-icalrow style="display: flex; flex-direction: column; gap: 6px; padding: 14px; border-radius: 14px; background: #FFFFFF; box-shadow: %s"><label for="%sic%d" style="font-size: 14px; font-weight: 600">Anuncio %d · enlace del calendario</label>'
      '<input id="%sic%d" data-ical placeholder="%s" style="height: 46px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 15px; font-family: inherit; color: #19194B; background: #FFFFFF">'
      '<div data-ical-ok hidden style="font-size: 13px; color: #0F7B4F; font-weight: 700">✓ Calendario conectado: 3 reservas encontradas</div></div>')%(SH,k,i,i,k,i,ph)
    help_=('<div class="stepin" style="display: grid; grid-template-columns: %s; gap: 10px">'%('1fr' if mob_ else '1fr 1fr')
      +card('<div style="font-size: 14px; font-weight: 700">Dónde está en Airbnb</div><div style="font-size: 13px; line-height: 1.5; color: #55557F">Calendario › Disponibilidad › Sincronizar calendarios › Exportar calendario. Copia el enlace.</div>',14)
      +card('<div style="font-size: 14px; font-weight: 700">Dónde está en Booking</div><div style="font-size: 13px; line-height: 1.5; color: #55557F">Tarifas y disponibilidad › Sincronizar calendarios › Exportar. Copia el enlace.</div>',14)+'</div>')
    return (ok('¡Buena elección! Las reservas entrarán solas.')+H('📅','Pega el enlace del calendario de cada anuncio','Uno por anuncio de Airbnb o Booking. Al pegarlo, te enseñamos las reservas que encontramos.',mob_)
      +help_+row(1,'https://www.airbnb.es/calendar/ical/…')+row(2,'https://admin.booking.com/…/ical…')
      +'<button type="button" data-addical style="align-self: flex-start; padding: 10px 14px; border: 1.5px dashed #385BF8; border-radius: 12px; background: transparent; color: #385BF8; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer">+ Añadir otro anuncio</button>'
      +'<div style="font-size: 13px; color: #55557F">Si conectas el calendario, no uses a la vez el enlace del chat de Airbnb: se duplicarían las reservas.</div>')
both('Calendario','Calendario',1,CH[:2]+['Calendario'],calendario,lambda Pp:back(Pp('Reservas'),'← Atrás'),lambda Pp:link(Pp('Paises'),'Ahora no')+btn(Pp('Paises'),'Continuar →'),lambda Pp:btn(Pp('Paises'),'Continuar →',full=True),lambda Pp:link(Pp('Paises'),'Ahora no'))
# ---------- 2a · Leído del PMS ----------
GR=[('🇪🇸','Madrid','España · SES.Hospedajes',2,50),(CAT,'Barcelona','Cataluña · Mossos d\'Esquadra',1,25),('🇵🇹','Lisboa','Portugal · SIBA',1,25)]
def cartera(Pp,mob_):
    scan=card('<div style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #385BF8">LEYENDO TU PMS</div><div class="scan1" style="font-size: 14px">✓ Contando tus viviendas</div><div class="scan2" style="font-size: 14px">✓ Situándolas en el mapa</div><div class="scan3" style="font-size: 14px">✓ Viendo qué normas aplican en cada zona</div>',14)
    stats='<div class="stepin" style="display: flex; gap: 30px"><div><div style="font-size: 34px; font-weight: 800"><span data-count="4">4</span></div><div style="font-size: 13px; color: #6B6B95">viviendas</div></div><div><div style="font-size: 34px; font-weight: 800"><span data-count="2">2</span></div><div style="font-size: 13px; color: #6B6B95">países</div></div><div><div style="font-size: 34px; font-weight: 800"><span data-count="3">3</span></div><div style="font-size: 13px; color: #6B6B95">zonas con normas propias</div></div></div>'
    rows=''.join(card('<div style="display: flex; gap: 12px; align-items: center"><div style="font-size: 22px; line-height: 1">%s</div><div style="flex-grow: 1"><div style="font-size: 15px; font-weight: 700">%s</div><div style="font-size: 13px; color: #6B6B95">%s</div></div><div style="font-size: 14px; font-weight: 700">%d viv.</div></div><div style="height: 5px; border-radius: 999px; background: #EFEFF7"><div style="height: 5px; width: %d%%; border-radius: 999px; background: #385BF8"></div></div>'%(f,n,c,k,pc),14,' class="stepin"') for f,n,c,k,pc in GR)
    return ok('¡<span class="pmsname">Cloudbeds</span> conectado! Ya tenemos tus viviendas.')+scan+H('','Esto nos ha dicho <span class="pmsname">Cloudbeds</span>','Las agrupamos por zona, porque cada una envía el parte a su policía.',mob_)+stats+rows+'<div style="font-size: 13px; color: #6B6B95">Solo lo hemos leído: en tu PMS no se ha tocado nada.</div>'
both('Cartera','Leído del PMS',2,CH[:2]+['Con PMS'],cartera,lambda Pp:back(Pp('Conectar'),'← Atrás'),lambda Pp:link(Pp('Paises'),'¿No es correcto? Ajústalo')+btn(Pp('Titular'),'Continuar →'),lambda Pp:btn(Pp('Titular'),'Continuar →',full=True),lambda Pp:link(Pp('Paises'),'¿No es correcto? Ajústalo'))
# ---------- 2b · Países ----------
TOP=[('🇪🇸','España','SES · Mossos · Ertzaintza','reg-es',True),('🇮🇹','Italia','Alloggiati Web','',False),('🇵🇹','Portugal','SIBA (AIMA)','',False)]
MORE=[('🇩🇪','Alemania','Meldeschein'),('🇦🇹','Austria','Gästeblatt'),('🇭🇷','Croacia','eVisitor'),('🇨🇭','Suiza','Parte a la policía'),('🇨🇿','Rep. Checa','Parte a la policía'),('🇧🇬','Bulgaria','ESTI'),('🇦🇪','EAU','Parte a la policía'),('🇧🇷','Brasil','Parte a la policía'),('🇨🇴','Colombia','Parte a la policía'),('🇫🇷','Francia','Formulario de entrada'),('🇬🇧','Reino Unido','Formulario de entrada'),('🇬🇷','Grecia','Formulario de entrada'),('🇳🇱','Países Bajos','Formulario de entrada'),('🇧🇪','Bélgica','Formulario de entrada'),('🇷🇴','Rumanía','Formulario de entrada')]
def pick(flag,name,sub,rev='',on=False):
    return ('<button type="button" class="pick%s"%s style="position: relative; display: flex; gap: 12px; align-items: center; padding: 14px 44px 14px 14px; border-radius: 14px; background: #FFFFFF; font-family: inherit; color: #19194B; text-align: left; cursor: pointer; min-height: 60px">'
      '<span class="pick-box" aria-hidden="true"></span><span style="font-size: 22px; line-height: 1">%s</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 700">%s</span><span style="font-size: 12px; color: #6B6B95">%s</span></span></button>')%(' on' if on else '',(' data-reveal="%s"'%rev) if rev else '',flag,name,sub)
def paises(Pp,mob_):
    cols=1 if mob_ else 3
    top=''.join(pick(f,n,a,r,o) for f,n,a,r,o in TOP)
    reg=('<div id="reg-es" class="stepin" style="display: flex; flex-direction: column; gap: 10px; padding: 14px; border-radius: 16px; background: #EFEFFF"><div style="font-size: 14px; font-weight: 700">🇪🇸 ¿En qué comunidades de España?</div>'
      '<div style="display: grid; grid-template-columns: repeat(%d, minmax(0, 1fr)); gap: 8px">'%cols+pick(CAT,'Cataluña',"Mossos d'Esquadra")+pick(EUS,'País Vasco','Ertzaintza')+pick('🇪🇸','Resto de España','SES.Hospedajes','',True)+'</div></div>')
    more='<div id="more-paises" hidden style="display: grid; grid-template-columns: repeat(%d, minmax(0, 1fr)); gap: 8px">%s</div>'%(1 if mob_ else 3,''.join(pick(f,n,a) for f,n,a in MORE))
    return (ok('¡Reservas listas! Ahora, dónde están tus viviendas.')
      +H('🗺️','¿Dónde están tus viviendas?','Marca todos los países. Activamos solo lo que pide la ley en cada uno.',mob_)
      +'<input type="search" placeholder="🔍  Busca un país" aria-label="Busca un país" style="height: 48px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 16px; font-family: inherit; background: #FFFFFF">'
      +'<div style="display: grid; grid-template-columns: repeat(%d, minmax(0, 1fr)); gap: 8px">%s</div>'%(cols,top)+reg
      +'<button type="button" data-more="more-paises" style="align-self: flex-start; padding: 10px 2px; border: 0; background: none; color: #385BF8; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer">+ Ver más países (15)</button>'+more)
both('Paises','Dónde están',2,CH[:2]+['Sin PMS'],paises,lambda Pp:back(Pp('Reservas'),'← Atrás'),lambda Pp:btn(Pp('Titular'),'Continuar →'),lambda Pp:btn(Pp('Titular'),'Continuar →',full=True))
# ---------- 3a · Titular ----------
def titular(Pp,mob_):
    k='m' if mob_ else 'p'
    return (ok('¡Ya sabemos dónde están! Ahora, quién es el titular.')
      +H('🪪','¿Quién es el titular de las viviendas?','La ley pide sus datos en cada parte de viajeros. Lo pones una vez y sirve para todas.',mob_)
      +card(field(k+'tn','Nombre o razón social','Katia Ruiz o Apartamentos Sol S.L.')
        +'<div data-nifbox>'+field(k+'tnif','NIF, NIE o CIF','12345678Z',extra=' data-nif inputmode="text" autocomplete="off"',hint='Lo comprobamos al escribirlo.')+'<div data-nif-ok hidden style="margin-top: 6px; font-size: 13px; color: #0F7B4F; font-weight: 700">✓ Formato correcto</div><div data-nif-ko hidden style="margin-top: 6px; font-size: 13px; color: #6B3E00">Casi: son 8 números y una letra (DNI), o una letra, 7 números y una letra o número (CIF).</div></div>'
        +'<label style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px; line-height: 1.45; cursor: pointer"><input type="checkbox" checked style="width: 20px; height: 20px; margin: 1px 0 0; accent-color: #385BF8"><span><b>El mismo titular para todas mis viviendas</b><br><span style="color: #6B6B95">¿Gestionas pisos de varios propietarios? Desmárcalo y lo pones en cada vivienda.</span></span></label>',18,' class="stepin"'))
both('Titular','Titular',3,CH,titular,lambda Pp:back(Pp('Paises'),'← Atrás'),lambda Pp:btn(Pp('Vivienda'),'Continuar →',NX%(Pp('Legal').replace('.dc.html',''),Pp('Vivienda').replace('.dc.html',''))),lambda Pp:btn(Pp('Vivienda'),'Continuar →',NX%(Pp('Legal').replace('.dc.html',''),Pp('Vivienda').replace('.dc.html','')),full=True))
# ---------- 3b · Vivienda una a una ----------
def vivienda(Pp,mob_):
    k='m' if mob_ else 'p'
    addr=('<div data-addr data-errbox style="display: flex; flex-direction: column; gap: 6px"><label for="%sva" style="font-size: 14px; font-weight: 600">Dirección</label>'
      '<input id="%sva" data-addr-input placeholder="Empieza a escribir: calle y número" autocomplete="off" style="height: 46px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 16px; font-family: inherit; background: #FFFFFF">')%(k,k)+(''
      '<div data-addr-list hidden style="border-radius: 12px; background: #FFFFFF; box-shadow: 0 12px 28px rgba(25, 25, 75, 0.14); overflow: hidden">'
      +''.join('<button type="button" data-addr-pick="%s" style="display: block; width: 100%%; padding: 12px 14px; border: 0; border-bottom: 1px solid #F0F0F7; background: #FFFFFF; text-align: left; font-size: 14px; font-family: inherit; cursor: pointer">📍 %s</button>'%(a,a) for a in ['Calle de San Juan, 12, 28012 Madrid','Calle de San Juan, 12, 46001 Valencia','Calle de San Juan de la Cruz, 12, Málaga'])
      +'<div style="padding: 6px 14px; font-size: 11px; color: #9696B9; text-align: right">con Google</div></div>'
      '<div data-addr-ok hidden style="font-size: 13px; color: #0F7B4F; font-weight: 700">✓ Dirección encontrada: ciudad, código postal y provincia, rellenos</div>'+errbox('No encontramos esa dirección. Revisa la calle y el número, o escríbela a mano y la comprobamos después.','Demo: dirección no encontrada')+'</div>')
    form=card('<div style="display: flex; justify-content: space-between; align-items: center"><div style="font-size: 13px; font-weight: 800; letter-spacing: 0.06em; color: #385BF8" data-vlabel>VIVIENDA 1 DE 4</div><div style="font-size: 12px; color: #6B6B95">⏱ ≈ 30 s</div></div>'
      +field(k+'vn','Nombre de la vivienda','Casa San Juan',extra=' data-vfield')+addr
,18,' class="stepin"')
    lst=card('<div style="font-size: 12px; font-weight: 800; letter-spacing: 0.06em; color: #6B6B95">TUS VIVIENDAS</div>'+''.join('<div data-vitem style="display: flex; gap: 10px; align-items: center; font-size: 14px"><span data-vdot style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 999px; border: 1.5px solid #C9CBEA; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; color: #FFFFFF"></span><span data-vname>Vivienda %d</span></div>'%i for i in range(1,5))+'<div style="font-size: 12px; color: #6B6B95">Titular y parte de viajeros, ya puestos para todas.</div>',16)
    done=('<div data-vdone hidden class="stepin" style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding: 26px 22px; border-radius: 18px; background: #FFFFFF; box-shadow: %s">'
      '<div class="crea-mark done" style="width: 64px; height: 64px; border-radius: 18px; background: #19194B; display: flex; align-items: center; justify-content: center"><svg class="crea-check" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></div>'
      '<div style="font-size: 22px; font-weight: 800">¡Bien hecho, Katia!</div><div style="font-size: 15px; line-height: 1.5; color: #6B6B95"><span data-vdone-t>Ya tenemos tu primera vivienda registrada.</span><br><span data-vdone-s>¿Seguimos con el resto? Te quedan 3, unos 30 s cada una.</span></div>'
      '<div style="display: flex; flex-direction: column; gap: 8px; width: 100%%; max-width: 340px; margin-top: 4px"><button type="button" data-vcontinue style="height: 50px; border: 0; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 16px; font-weight: 700; font-family: inherit; cursor: pointer; box-shadow: 0 6px 16px rgba(56, 91, 248, 0.28)">Sí, seguir con la vivienda <span data-vnextn>2</span></button>'
      '<a href="%s" data-vfinish style="display: block; height: 48px; line-height: 44px; box-sizing: border-box; border-radius: 12px; border: 2px solid #C9CBEA; color: #19194B; font-size: 15px; font-weight: 700; text-decoration: none">Termino aquí y sigo con el resto del alta</a>'
      '<div style="font-size: 12px; color: #6B6B95">Podrás añadir las demás cuando quieras desde Viviendas.</div></div></div>')%(SH,Pp('Legal'))
    form='<div data-vform>'+form+'</div>'
    head=ok('¡Titular listo! Ahora, tus viviendas, una a una.')+H('🏠','Añade tus viviendas','Solo nombre y dirección, de una en una. Escribe la calle y elígela de la lista.',mob_)
    if mob_: return head+form+done+lst
    return head+'<div style="display: grid; grid-template-columns: 1fr 210px; gap: 16px; align-items: start"><div>'+form+done+'</div>'+lst+'</div>'
both('Vivienda','Tus viviendas',3,CH,vivienda,lambda Pp:back(Pp('Titular'),'← Atrás'),lambda Pp:btn(Pp('Legal'),'Guardar vivienda ✓',' data-vnext data-vtotal="4"'),lambda Pp:btn(Pp('Legal'),'Guardar vivienda ✓',' data-vnext data-vtotal="4"',full=True),wide=True)
# ---------- 4 · Parte de viajeros ----------
def ses_fields(k):
    return (field(k+'sa','Código de arrendador','Ej.: 0000012345',hint='Te lo dio SES al darte de alta como arrendador.')
      +'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">'+field(k+'su','Usuario del servicio web','Termina en WS')+field(k+'sp','Contraseña del servicio web','••••••••','password')+'</div>'
      +'<div style="font-size: 12px; line-height: 1.45; color: #6B3E00; background: #FFF4E5; padding: 8px 10px; border-radius: 10px">No son el email ni la contraseña del portal de SES: son las credenciales del servicio web, que se piden aparte.</div>'+'<div style="font-size: 14px; font-weight: 600; margin-top: 4px">Código de establecimiento de cada vivienda <span style="font-weight: 400; color: #6B6B95">(opcional ahora)</span></div>'+'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">'+field(k+'e1','Casa San Juan','Código SES')+field(k+'e2','Madrid Sol','Código SES')+'</div>')
def gen_fields(k,a,hint=''): return '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">'+field(k+'gu','Usuario de '+a,'Tu usuario')+field(k+'gp','Contraseña','••••••••','password')+'</div>'+(('<div style="font-size: 12px; line-height: 1.45; color: #6B6B95">%s</div>'%hint) if hint else '')
def legal(Pp,mob_):
    k='m' if mob_ else 'p'
    def grp(n_,flag,zona,nv,a,fields,errmsg):
        fid='%slf%d'%(k,n_); hid='%slh%d'%(k,n_)
        btn2=('<div style="display: flex; flex-wrap: wrap; gap: 8px">'
          '<button type="button" data-acc="%s" style="flex: 1; min-width: 150px; height: 46px; border: 0; border-radius: 12px; background: #EFEFFF; color: #19194B; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer">No los tengo: ayúdame</button>'
          '<button type="button" data-acc="%s" style="flex: 1; min-width: 150px; height: 46px; border: 2px solid #C9CBEA; border-radius: 12px; background: #FFFFFF; color: #19194B; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer">Tengo los datos</button></div>')%(hid,fid)
        helpp=('<div id="%s" data-accp hidden style="display: flex; flex-direction: column; gap: 8px; padding: 12px; border-radius: 12px; background: #F4F6FF">'
          '<div style="font-size: 14px; font-weight: 700">Sin prisa: sigue con el alta y lo dejamos como tarea en tu Inicio.</div>'
          '<a href="#" style="font-size: 14px; font-weight: 700; text-decoration: none">▶ Cómo conseguirlos, paso a paso (vídeo)</a>'
          '<a href="#" style="font-size: 14px; font-weight: 700; text-decoration: none">Un experto en Chekin lo hace contigo</a>'
          '%s<button type="button" data-later style="align-self: flex-start; padding: 8px 0; border: 0; background: none; color: #385BF8; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer">Recuérdamelo mañana</button></div>')%(hid,'<a href="#" style="font-size: 14px; font-weight: 700; text-decoration: none">📧 Mándamelo al ordenador</a>' if mob_ else '')
        formp=('<div id="%s" data-accp data-errbox hidden style="display: flex; flex-direction: column; gap: 10px">'%fid+fields+errbox(errmsg,'Demo: datos incorrectos')+LOCK%('Se guardan cifradas y solo se usan para enviar tus partes a '+a+'. Puedes borrarlas cuando quieras.')
          +'<button type="button" data-connect style="height: 48px; border: 0; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 15px; font-weight: 700; font-family: inherit; cursor: pointer">Conectar %s</button></div>'%a)
        return card('<div style="display: flex; gap: 12px; align-items: center"><div style="font-size: 22px; line-height: 1">%s</div><div style="flex-grow: 1"><div style="font-size: 16px; font-weight: 700">%s</div><div style="font-size: 13px; color: #6B6B95">%s · el parte va a <b>%s</b></div></div><span data-lstat style="padding: 3px 8px; border-radius: 999px; background: #FFF4E5; color: #6B3E00; font-size: 12px; font-weight: 700; white-space: nowrap">Pendiente</span></div>'%(flag,zona,nv,a)
          +btn2+helpp+formp,16,' class="stepin"')
    extras=card('<div style="font-size: 15px; font-weight: 700">Para todas tus viviendas</div>'
      +'<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px"><div><div style="font-size: 14px; font-weight: 700">Verificación de identidad</div><div style="font-size: 12px; color: #6B6B95">Documento + selfie de cada huésped. Antes de la selfie, el huésped da su consentimiento.</div></div>'+sw(True,'Verificación de identidad')+'</div>'
      +'<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px"><div><div style="font-size: 14px; font-weight: 700">Tasa turística</div><div style="font-size: 12px; color: #6B6B95">Solo donde tu municipio la cobra</div></div>'+sw(False,'Tasa turística')+'</div>',16,' class="stepin"')
    return (ok('¡Vamos con el paso legal!')
      +H('🛡️','Conecta tu parte de viajeros','Es lo que permite enviar el check-in a tus huéspedes. Ve de una autoridad en una: si no tienes los datos ahora, sigue y te ayudamos después.',mob_)
      +grp(1,'🇪🇸','Madrid','2 viviendas','SES.Hospedajes',ses_fields(k),'SES no acepta estos datos. Revisa el usuario del servicio web (termina en WS) y su contraseña: no son los del portal.')
      +grp(2,CAT,'Barcelona','1 vivienda',"Mossos d'Esquadra",gen_fields(k+'m',"Mossos",'Los del establecimiento: te los dan los Mossos al dar de alta la vivienda.'),'Los Mossos no aceptan estos datos. Revisa el usuario y la contraseña del establecimiento.')
      +grp(3,'🇵🇹','Lisboa','1 vivienda','SIBA (AIMA)',gen_fields(k+'s','SIBA','Los de acceso al SIBA de tu alojamiento.'),'El SIBA no acepta estos datos. Revisa el usuario y la contraseña.')
      +extras
      +'<div style="font-size: 13px; color: #55557F">Lo que dejes pendiente aparece como tarea en tu Inicio. Cl@ve o el certificado digital solo sirven para darte de alta: a nosotros no nos los das.</div>')
both('Legal','Parte de viajeros',4,CH+['Titular ✓'],legal,lambda Pp:link(Pp('Vivienda'),'← Atrás',NX%(Pp('Titular').replace('.dc.html',''),Pp('Vivienda').replace('.dc.html',''))),lambda Pp:btn(Pp('Proteccion'),'Continuar →'),lambda Pp:btn(Pp('Proteccion'),'Continuar →',full=True),wide=True)
# ---------- 5 · Protección ----------
ALL1='<button type="button" data-allon class="stepin" style="height: 48px; border: 0; border-radius: 12px; background: #EFEFFF; color: #385BF8; font-size: 15px; font-weight: 700; font-family: inherit; cursor: pointer">Activar las dos en un clic</button>'
ALL2='<button type="button" data-allon class="stepin" style="height: 48px; border: 0; border-radius: 12px; background: #EFEFFF; color: #385BF8; font-size: 15px; font-weight: 700; font-family: inherit; cursor: pointer">Activar las 4 en un clic</button>'
def prot(Pp,mob_):
    q='<span title="Más información" style="display: inline-flex; width: 18px; height: 18px; border-radius: 999px; border: 1.5px solid #C9CBEA; color: #6B6B95; font-size: 11px; font-weight: 800; align-items: center; justify-content: center; vertical-align: 1px; margin-left: 4px">?</span>'
    ben=('<div class="stepin" style="display: flex; flex-direction: column; gap: 8px; font-size: 14px; line-height: 1.5">'
      '<div><span style="color: #0F7B4F; font-weight: 800">✓</span> <b>Respaldo económico.</b> <span style="color: #6B6B95">Tus viviendas, cubiertas ante lo que nadie vio venir.</span></div>'
      '<div><span style="color: #0F7B4F; font-weight: 800">✓</span> <b>Cobro inmediato.</b> <span style="color: #6B6B95">El dinero llega online al hacer el check-in, no después de perseguir a nadie.</span></div></div>')
    video=('<div role="img" aria-label="Vídeo: cómo funciona la protección de daños" class="stepin" style="position: relative; height: %dpx; border-radius: 16px; overflow: hidden; background: linear-gradient(135deg, #385BF8 0%%, #2E3B9E 60%%, #19194B 100%%); color: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px">'
      '<div style="position: absolute; top: 12px; left: 14px; font-size: 12px; font-weight: 700; color: #DCE3FF">Fianza y protección</div>'
      '<span style="width: 52px; height: 52px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2)"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="#385BF8"></path></svg></span>'
      '<div style="font-size: 14px; font-weight: 700">Cómo funciona la protección de daños · 1 min</div></div>')%(150 if mob_ else 170)
    def item(t,amt,sub,lab): return ('<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 6px; padding: 14px 16px">'
      '<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px"><div style="font-size: 15px; font-weight: 700">%s%s</div>%s</div>'
      '<div style="font-size: 18px; font-weight: 800">%s</div><div style="font-size: 13px; line-height: 1.45; color: #6B6B95">%s</div><a href="#" style="font-size: 13px; font-weight: 700; text-decoration: none">Ajustes</a></div>')%(t,q,sw(False,lab),amt,sub)
    a=item('Protección de daños','Hasta 2.500 €','27,20 € por estancia, lo paga el huésped.','Protección de daños')
    b=item('Fianza','200 € que se devuelven','Vuelven a su cuenta 7 días después de la salida.','Fianza')
    grp=('<div class="stepin" style="border-radius: 16px; background: #FFFFFF; box-shadow: %s; overflow: hidden">'
      '<div style="display: flex; gap: 12px; align-items: center; padding: 14px 16px; background: #F4F6FF; border-bottom: 1px solid #ECECF5"><div aria-hidden="true" style="width: 36px; height: 36px; border-radius: 10px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">🛡️</div>'
      '<div style="flex-grow: 1"><div style="font-size: 15px; font-weight: 700">Todas tus viviendas</div><div style="font-size: 12px; color: #6B6B95">Se aplica a todo lo que añadas, hasta que las separes en grupos.</div></div><a href="#" style="font-size: 13px; font-weight: 700; text-decoration: none">Separar por grupos</a></div>'
      '<div style="display: flex; %s">%s<div style="%s"></div>%s</div>'
      '<div style="padding: 10px 16px; border-top: 1px solid #ECECF5; font-size: 13px; color: #6B6B95">En el check-in, el huésped elige: <b style="color: #19194B">27,20 € de protección</b> o <b style="color: #19194B">200 € de fianza</b>, que se devuelve 7 días después de la salida.</div></div>')%(SH,'flex-direction: column' if mob_ else '',a,'height: 1px; background: #ECECF5' if mob_ else 'width: 1px; background: #ECECF5',b)
    head=ok('Vas genial. Ahora, que nada te salga caro.')+H('','Protege tus viviendas de daños','Las cosas se rompen, y la factura llega lo hayas previsto o no. Con Chekin, la cubre el huésped.',mob_)
    if mob_: return head+ben+video+grp+ALL1+'<div class="stepin" style="font-size: 13px; line-height: 1.5; color: #55557F">Vienen apagadas: tú eliges. <b style="color: #19194B">Quién cobra:</b> Chekin, al huésped, en el check-in. <a href="#" style="font-weight: 700">Comisiones</a> · <a href="#" style="font-weight: 700">Cómo se reclama un daño</a></div>'
    return head+'<div style="display: grid; grid-template-columns: 1fr 280px; gap: 18px; align-items: center">'+ben+video+'</div>'+grp+ALL1+'<div class="stepin" style="font-size: 13px; line-height: 1.5; color: #55557F">Vienen apagadas: tú eliges. <b style="color: #19194B">Quién cobra:</b> Chekin, al huésped, en el check-in. <a href="#" style="font-weight: 700">Comisiones</a> · <a href="#" style="font-weight: 700">Cómo se reclama un daño</a></div>'
both('Proteccion','Protección',5,CH+['Parte ✓'],prot,lambda Pp:back(Pp('Legal'),'← Atrás'),lambda Pp:link(Pp('Ventas'),'Ahora no')+btn(Pp('Ventas'),'Seguir →'),lambda Pp:btn(Pp('Ventas'),'Seguir →',full=True),lambda Pp:link(Pp('Ventas'),'Ahora no'),wide=True)
# ---------- 6 · Ventas extra ----------
INPS='height: 44px; border-radius: 10px; border: 1.5px solid #DEDEEB; background: #FFFFFF; font-size: 15px; font-weight: 700; font-family: inherit; color: #19194B'
def vprice(units,val=''):
    opts=''.join('<option>%s</option>'%u for u in units)
    return ('<div data-price hidden style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center; padding-top: 2px">'
      '<input data-pv value="%s" placeholder="0" inputmode="decimal" aria-label="Precio" style="width: 72px; text-align: center; %s"><span style="font-size: 15px; font-weight: 700">€</span>'
      '<select data-pu aria-label="Cómo se cobra" style="padding: 0 10px; %s">%s</select></div>')%(val,INPS,INPS,opts)
# Lo básico: preguntas de sí o no
VQ=[('q1','🕐','¿Dejas entrar antes de la hora?','Entrada anticipada',['por reserva'],'20'),
    ('q2','🌙','¿Y salir más tarde?','Salida tardía',['por reserva'],'20'),
    ('q3','🐾','¿Aceptas mascotas?','Mascota',['por noche y mascota','por estancia y mascota'],'10'),
    ('q4','🚗','¿Tienes aparcamiento?','Aparcamiento',['por noche','por reserva'],'10')]
def vq(g,ic,q,name,units,val):
    yn=lambda v,t:'<button type="button" class="chip" data-yn="%s" data-group="%s" aria-pressed="false" style="height: 44px; width: 60px; font-size: 15px">%s</button>'%(v,g,t)
    return card('<div data-offer data-name="%s" style="display: flex; flex-direction: column; gap: 10px">'
      '<div style="display: flex; flex-wrap: wrap; gap: 10px 12px; align-items: center"><div aria-hidden="true" style="font-size: 22px; line-height: 1">%s</div>'
      '<div style="flex: 1; min-width: 110px"><div style="font-size: 15px; font-weight: 700">%s</div><div style="font-size: 13px; color: #55557F">%s</div></div>'
      '<div role="group" aria-label="%s" style="display: flex; gap: 6px; margin-left: auto">%s%s</div></div>%s</div>'%(name,ic,q,name,q,yn('1','Sí'),yn('0','No'),vprice(units,val)),14,' class="stepin"')
# Todos los demás extras
VC=[('🥐','Desayuno',['por persona y noche','por persona']),('🧺','Cesta de bienvenida',['por reserva']),
    ('✈️','Traslado al aeropuerto',['por trayecto','por reserva']),('🚲','Alquiler de bicis',['por día','por reserva']),
    ('🧹','Limpieza extra',['por servicio']),('🛏️','Cuna o trona',['por estancia','por noche']),
    ('🛁','Cambio de sábanas y toallas',['por servicio']),('🎟️','Excursiones y entradas',['por persona','por reserva'])]
def vc(ic,name,units):
    return ('<div data-offer data-name="%s" style="display: flex; flex-direction: column; gap: 8px">'%name+pick(ic,name,units[0])+vprice(units)+'</div>')
def ventas(Pp,mob_):
    basics=''.join(vq(*q) for q in VQ)
    cat=''.join(vc(*c) for c in VC)
    own=('<div data-offer data-name="Tu oferta" style="display: flex; flex-direction: column; gap: 8px">'+pick('✏️','Crea tu propia oferta','Lo que tú quieras vender')
      +'<div data-price hidden style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center"><input data-oname placeholder="Nombre (ej.: botella de vino)" aria-label="Nombre de la oferta" style="flex: 1; min-width: 160px; padding: 0 12px; font-weight: 500; %s"><input data-pv placeholder="0" inputmode="decimal" aria-label="Precio" style="width: 72px; text-align: center; %s"><span style="font-size: 15px; font-weight: 700">€</span><select data-pu aria-label="Cómo se cobra" style="padding: 0 10px; %s"><option>por reserva</option><option>por noche</option><option>por persona</option></select></div></div>')%(INPS,INPS,INPS)
    more=('<details class="stepin" data-vmore style="border-radius: 16px; background: #FFFFFF; box-shadow: %s">'
      '<summary style="list-style: none; cursor: pointer; display: flex; gap: 12px; align-items: center; padding: 16px; font-family: inherit"><div aria-hidden="true" style="font-size: 22px">✨</div><div style="flex-grow: 1"><div style="font-size: 15px; font-weight: 700">¿Quieres ganar más? Mira todos los extras</div><div style="font-size: 13px; color: #55557F">Desayuno, traslados, limpieza, cuna… y los que tú crees</div></div><span data-vmore-i style="font-size: 14px; font-weight: 700; color: #385BF8; white-space: nowrap">Ver %d más ▾</span></summary>'
      '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 0 16px 16px">%s%s</div></details>')%(SH,len(VC),cat,own)
    note='<div class="stepin" style="font-size: 13px; line-height: 1.5; color: #55557F">Nada viene activado: solo sale lo que elijas. Precios de ejemplo: pon los tuyos. El huésped paga con tarjeta y te llega el importe menos la comisión de Chekin. <a href="#" style="font-weight: 700">Comisiones</a></div>'
    phone=('<div class="stepin" style="width: %s; box-sizing: border-box; border: 7px solid #161643; border-radius: 28px; background: #FFFFFF; padding: 12px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 18px 30px rgba(25, 25, 75, 0.18); align-self: center">'
      '<div style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #55557F">ASÍ LO VE TU HUÉSPED</div><div style="padding: 9px 11px; border-radius: 12px; background: #161643; color: #FFFFFF; font-size: 13px"><b>Casa San Juan</b><br><span style="color: #C9CBEA">12 – 15 mar · 3 noches</span></div>'
      '<div style="font-size: 13px; font-weight: 800; color: #385BF8">Añade a tu estancia</div><div data-vprev aria-live="polite" style="display: flex; flex-direction: column; gap: 6px"></div>'
      '<div data-vempty style="padding: 14px 10px; border-radius: 12px; border: 1.5px dashed #DEDEEB; font-size: 13px; line-height: 1.4; color: #55557F; text-align: center">Aquí verás lo que le ofreces</div></div>')%('100%' if mob_ else '260px')
    head=(ok('Vas genial. Ahora, gana más con cada reserva.')
      +H('💶','¿Qué más le ofreces a tu huésped?','Empecemos por lo básico: contesta sí o no. Lo que actives sale en su check-in y lo paga antes de llegar.',mob_))
    if mob_: return head+basics+more+note+'<div class="stepin" style="font-size: 15px; font-weight: 700; margin-top: 4px">Así lo verá tu huésped</div>'+phone.replace('<div style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #55557F">ASÍ LO VE TU HUÉSPED</div>','')
    return head+'<div style="display: grid; grid-template-columns: 1fr 260px; gap: 22px; align-items: start"><div style="display: flex; flex-direction: column; gap: 10px">'+basics+more+note+'</div><div style="position: sticky; top: 0; display: flex">'+phone+'</div></div>'
both('Ventas','Ventas extra',6,CH+['Protección ✓'],ventas,lambda Pp:back(Pp('Proteccion'),'← Atrás'),lambda Pp:link(Pp('Envio'),'Ahora no')+btn(Pp('Envio'),'Seguir →'),lambda Pp:btn(Pp('Envio'),'Seguir →',full=True),lambda Pp:link(Pp('Envio'),'Ahora no'),wide=True)
# ---------- 7 · Envío ----------
def envio(Pp,mob_):
    when='<div style="display: flex; flex-wrap: wrap; gap: 8px">'+''.join('<button type="button" class="chip%s" data-group="cuando" data-val="%s" style="height: 44px; padding: 0 14px; font-size: 14px">%s</button>'%(' on' if v=='48 h antes' else '',v,v) for v in ['Al confirmar','72 h antes','48 h antes','24 h antes'])+'</div>'
    send=card('<div style="display: flex; justify-content: space-between; align-items: center; gap: 12px"><div><div style="font-size: 15px; font-weight: 700">Enviar el check-in automáticamente</div><div style="font-size: 13px; color: #6B6B95">Por email y WhatsApp, en su idioma.</div></div>'+sw(True,'Envío automático')+'</div><div style="font-size: 14px; font-weight: 700; margin-top: 4px">¿Cuándo?</div>'+when+'<div style="font-size: 12px; color: #6B6B95">Si la reserva entra más tarde, sale al momento.</div>',18,' class="stepin"')
    phone=('<div class="stepin" style="width: 250px; box-sizing: border-box; border: 7px solid #161643; border-radius: 28px; background: #FFFFFF; padding: 12px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 18px 30px rgba(25, 25, 75, 0.18); align-self: center">'
      '<div style="font-size: 10px; font-weight: 800; letter-spacing: 0.08em; color: #6B6B95">ASÍ LO VE TU HUÉSPED</div><div style="padding: 9px 11px; border-radius: 12px; background: #161643; color: #FFFFFF; font-size: 12px"><b>Casa San Juan</b><br><span style="color: #C9CBEA">12 – 15 mar</span></div>'
      '<div style="padding: 9px 11px; border-radius: 12px; background: #F4F4FD; font-size: 12px"><b>Documento + selfie</b></div><div style="padding: 9px 11px; border-radius: 12px; background: #F4F4FD; font-size: 12px"><b>Protección o fianza</b></div>'
      '<div style="padding: 9px 11px; border-radius: 12px; background: #EFEFFF; font-size: 12px"><b style="color: #385BF8">Añade a tu estancia</b><br>Salida tardía · 20 €</div></div>')
    test='<button type="button" data-connect style="height: 46px; border: 1.5px solid #385BF8; border-radius: 12px; background: #FFFFFF; color: #385BF8; font-size: 15px; font-weight: 700; font-family: inherit; cursor: pointer">📲 Enviarme un enlace de prueba</button>'
    top=ok('¡Último paso!')+H('','¿Cuándo le llega el check-in a tu huésped?','Elige si sale solo y con cuánta antelación. Y pruébalo tú antes que nadie.',mob_)
    if mob_: return top+send+test+phone
    return top+'<div style="display: grid; grid-template-columns: 1fr 250px; gap: 22px; align-items: start"><div style="display: flex; flex-direction: column; gap: 12px">'+send+test+'</div>'+phone+'</div>'
both('Envio','Check-in y envío',7,CH+['4 ofertas ✓'],envio,lambda Pp:back(Pp('Ventas'),'← Atrás'),lambda Pp:btn(Pp('Listo'),'Terminar ✓'),lambda Pp:btn(Pp('Listo'),'Terminar ✓',full=True),wide=True)
# ---------- ¡Todo listo! (revelado ✓ a ✓) ----------
DONE=[('Reservas','<span data-done-res>entran solas desde tu PMS</span>'),('Titular y viviendas','<span data-done-viv>4 viviendas listas</span>'),('Parte de viajeros','<span data-done-legal>sale solo y en plazo</span>'),('Verificación de identidad','<span data-done-opt="id">documento + selfie</span>'),('Tasa turística','<span data-done-opt="tax">calculada y cobrada</span>'),('Protección y fianza','<span data-done-opt="prot">las paga el huésped</span>'),('Ventas extra','<span data-done-opt="ven">activas en el check-in</span>'),('Check-in automático','48 h antes de cada llegada')]
def listo(Pp,mob_):
    lst=''.join('<div class="ri" style="display: flex; gap: 12px; align-items: center; font-size: 15px"><span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 999px; background: #0F7B4F; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800">✓</span><span><b>%s</b> · %s</span></div>'%(a,b) for a,b in DONE)
    return ('<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding-top: 8px">'
      '<div class="crea-mark done" style="width: 88px; height: 88px; border-radius: 24px; background: #19194B; display: flex; align-items: center; justify-content: center"><svg class="crea-check" width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></div>'
      '<h1 style="margin: 0; font-size: %dpx; font-weight: 800">¡Todo listo, Katia!</h1><p style="margin: 0; font-size: 15px; color: #6B6B95">Esto ya funciona solo:</p></div>'%(24 if mob_ else 28)
      +card(lst,20)+'<div class="ri" style="font-size: 14px; color: #6B6B95; text-align: center">Ahora solo quedan tus reservas: en cada una eliges si se envía el check-in y cuándo.</div>'+'<div class="ri" style="font-size: 13px; color: #55557F; text-align: center">Tu prueba gratis acaba el 17 de noviembre. Sin tarjeta y sin permanencia: te avisamos antes para que elijas plan.</div>')
W(M('Listo'),mob('¡Todo listo!',0,listo(M,True),'<span class="ri-btn" style="width: 100%"><a href="PanelNuevo.dc.html" style="display: block; height: 58px; line-height: 58px; border-radius: 16px; background: #385BF8; color: #FFFFFF; font-size: 18px; font-weight: 800; text-align: center; text-decoration: none; box-shadow: 0 12px 28px rgba(56, 91, 248, 0.35)">Entrar en mi panel →</a></span>'))
W(P('Listo'),lap('¡Todo listo!',8,CH+['Todo ✓'],listo(P,False)+'<div class="ri-btn" style="display: flex; justify-content: center; padding-top: 6px"><a href="Portatil-PanelNuevo.dc.html" style="display: inline-block; height: 60px; line-height: 60px; padding: 0 44px; border-radius: 16px; background: #385BF8; color: #FFFFFF; font-size: 18px; font-weight: 800; text-decoration: none; box-shadow: 0 12px 28px rgba(56, 91, 248, 0.35)">Entrar en mi panel →</a></div>','','',center=True))
# ---------- Inicio ----------
PLAN_EJ=39
def panel(mob_):
    G2=('<div style="display: grid; grid-template-columns: %s; gap: 14px; align-items: start">')%('1fr' if mob_ else '1.55fr 1fr')
    def sec(t,link=''): return '<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 10px"><h2 style="margin: 0; font-size: 18px; font-weight: 800">%s</h2>%s</div>'%(t,link)
    def chip(t,c,bg): return '<span style="display: inline-block; padding: 3px 8px; border-radius: 999px; background: %s; color: %s; font-size: 12px; font-weight: 700; white-space: nowrap">%s</span>'%(bg,c,t)
    OK=('#0F5C3B','#E8F6EF'); WARN=('#6B3E00','#FFF4E5'); INFO=('#385BF8','#EFEFFF')
    # 1. Estado de la operación
    hero=('<section class="stepin" style="display: flex; gap: 16px; align-items: center; justify-content: space-between; padding: 20px 22px; border-radius: 20px; background: linear-gradient(135deg, #19194B, #2E3B9E); color: #FFFFFF">'
      '<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-size: 12px; color: #C9CBEA">Lunes 2 de noviembre</div><h1 style="margin: 0; font-size: %dpx; font-weight: 800">Todo en orden, Katia</h1>'
      '<div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: #DCE3FF"><span>✓ 4 viviendas listas</span><span>✓ Partes al día</span><span style="color: #FFD58A">● 1 cosa que revisar</span></div></div>'
      '<a href="#" style="flex-shrink: 0; padding: 10px 14px; border-radius: 12px; background: #FFFFFF; color: #19194B; font-size: 14px; font-weight: 800; text-decoration: none">Crear reserva</a></section>')%(22 if mob_ else 26)
    kp=[('Llegadas hoy','2','Casa San Juan · Madrid Sol'),('Próximos 7 días','6 llegadas','14 huéspedes'),('Check-in online','5 de 6','hechos antes de llegar'),('Partes a la policía','31 enviados','0 pendientes este mes')]
    tiles='<div style="display: grid; grid-template-columns: repeat(%d, minmax(0, 1fr)); gap: 10px">'%(2 if mob_ else 4)+''.join(card('<div style="font-size: 12px; color: #6B6B95">%s</div><div style="font-size: 22px; font-weight: 800">%s</div><div style="font-size: 12px; color: #6B6B95">%s</div>'%k,14,' class="stepin"') for k in kp)+'</div>'
    falta=card(sec('Lo que falta')+'<div style="display: flex; gap: 12px; align-items: center; padding: 12px; border-radius: 12px; background: #FFF4E5"><span style="font-size: 20px">🪪</span><div style="flex-grow: 1"><div style="font-size: 14px; font-weight: 700; color: #6B3E00">Marco Bianchi aún no ha subido su documento</div><div style="font-size: 12px; color: #6B3E00">Llega mañana a las 17:30 · Barcelona Centro. Sin documento no se puede enviar su parte.</div></div><a href="#" style="flex-shrink: 0; font-size: 13px; font-weight: 800; color: #6B3E00">Reenviar enlace</a></div><div style="font-size: 13px; color: #6B6B95">Nada más pendiente. Te avisamos aquí en cuanto falte algo.</div>',16,' class="stepin"')
    LEG=[('🇪🇸','SES.Hospedajes','Madrid · 2 viviendas'),(CAT,"Mossos d'Esquadra",'Barcelona · 1 vivienda'),('🇵🇹','SIBA (AIMA)','Lisboa · 1 vivienda')]
    legal=card(sec('Parte de viajeros')+'<div style="font-size: 13px; color: #6B6B95">Obligatorio por ley y necesario para enviar el check-in a tus huéspedes.</div>'+''.join('<div style="display: flex; gap: 10px; align-items: center; padding: 8px 0; border-top: 1px solid #F0F0F7"><span style="font-size: 18px; width: 24px">%s</span><div style="flex-grow: 1"><div style="font-size: 14px; font-weight: 700">%s</div><div style="font-size: 12px; color: #6B6B95">%s</div></div>%s</div>'%(f,a,b,chip('✓ Conectado',*OK)) for f,a,b in LEG),16,' class="stepin"')
    VV=[('Casa San Juan','Madrid','SES'),('Madrid Sol','Madrid','SES'),('Barcelona Centro','Barcelona','Mossos'),('Lisboa Alfama','Lisboa','SIBA')]
    viv=card(sec('Tus viviendas','<a href="#" style="font-size: 13px; font-weight: 700; text-decoration: none">Ver todas</a>')+''.join('<div style="display: flex; gap: 10px; align-items: center; padding: 8px 0; border-top: 1px solid #F0F0F7"><span style="font-size: 18px">🏠</span><div style="flex-grow: 1"><div style="font-size: 14px; font-weight: 700">%s</div><div style="font-size: 12px; color: #6B6B95">%s · parte a %s · check-in automático</div></div>%s</div>'%(n,c,a,chip('✓ Lista',*OK)) for n,c,a in VV),16,' class="stepin"')
    # 2. Próximas reservas
    BK=[('Hoy · 15:00','Lena Fischer','Casa San Juan','2 huéspedes · 3 noches',('✓ Check-in hecho',)+OK,'Enviado'),
        ('Hoy · 18:00','Tom Weber','Madrid Sol','1 huésped · 2 noches',('✓ Check-in hecho',)+OK,'Enviado'),
        ('Mañana · 17:30','Marco Bianchi','Barcelona Centro','2 huéspedes · 4 noches',('Falta el documento',)+WARN,'Enviado'),
        ('Jue 5 · 16:00','Ana Souza','Lisboa Alfama','3 huéspedes · 5 noches',('Se envía 48 h antes',)+INFO,'48 h antes'),
        ('Sáb 7 · 15:00','Familia Ortega','Casa San Juan','4 huéspedes · 7 noches',('Se envía 48 h antes',)+INFO,'48 h antes')]
    rows=''.join('<div style="display: flex; gap: 10px; align-items: center; padding: 11px 0; border-top: 1px solid #F0F0F7; flex-wrap: %s"><div style="width: %s; flex-shrink: 0; font-size: 12px; color: #6B6B95; font-weight: 700">%s</div><div style="flex-grow: 1; min-width: 0"><div style="font-size: 14px; font-weight: 700">%s · <span style="font-weight: 500">%s</span></div><div style="font-size: 12px; color: #6B6B95">%s</div></div>%s<div style="display: flex; align-items: center; gap: 6px"><span style="font-size: 11px; color: #6B6B95; white-space: nowrap">Envío: %s</span>%s</div></div>'%('wrap' if mob_ else 'nowrap','100%' if mob_ else '96px',d,n,p,g,chip(*st),w,sw(True,'Enviar check-in a '+n)) for d,n,p,g,st,w in BK)
    res=card(sec('Próximas reservas','<a href="#" style="font-size: 13px; font-weight: 700; text-decoration: none">Ver las 38 de este mes</a>')+'<div style="font-size: 13px; color: #6B6B95">6 llegadas en los próximos 7 días · 14 huéspedes. En cada reserva eliges si se envía el check-in y cuándo.</div>'+rows,18,' class="stepin"')
    # 3. Ventas extra: que se pagan Chekin
    WK=[('Sem. 1',25),('Sem. 2',40),('Sem. 3',45),('Sem. 4',55)]
    mx=max(v for _,v in WK)
    bars=''.join('<div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 6px; height: 100%%"><div style="font-size: 12px; font-weight: 700">%d €</div><div class="wbar" style="width: 66%%; height: %d%%; border-radius: 8px 8px 4px 4px; background: linear-gradient(180deg, #4FA3F7, #385BF8)"></div><div style="font-size: 11px; color: #6B6B95">%s</div></div>'%(v,round(100*v/mx*0.7),w) for w,v in WK)
    chart='<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 13px; font-weight: 700">Ingresos por semana</div><div role="img" aria-label="Ingresos por extras por semana: 25, 40, 45 y 55 euros" style="display: flex; gap: 8px; align-items: flex-end; height: 130px; border-bottom: 1px solid #ECECF5">'+bars+'</div></div>'
    meses=165/PLAN_EJ
    roi=('<div style="display: flex; gap: 16px; align-items: center; padding: 16px 18px; border-radius: 16px; background: linear-gradient(135deg, #E8F6EF, #DFF5F0)">'
      '<div style="font-size: 34px; line-height: 1">🎉</div><div style="flex-grow: 1"><div style="font-size: 17px; font-weight: 800; color: #0F5C3B">Este mes, tus extras pagan Chekin</div>'
      '<div style="font-size: 14px; line-height: 1.5; color: #0F5C3B">Tus extras han generado <b>165 €</b>: pagan <b>%d meses</b> de tu suscripción de Chekin (%d €/mes).</div></div></div>')%(165//PLAN_EJ,PLAN_EJ)
    kps=[('Ingresos por extras','165 €'),('Ventas','10'),('Huéspedes que compran','15,6 %'),('Ticket medio','16,5 €')]
    mini='<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">'+''.join('<div style="padding: 10px 12px; border-radius: 12px; background: #F4F6FF"><div style="font-size: 12px; color: #6B6B95">%s</div><div style="font-size: 18px; font-weight: 800">%s</div></div>'%k for k in kps)+'</div>'
    protf=('<div style="display: flex; flex-wrap: wrap; gap: 8px">'+chip('🛡️ Protección activa · 7 estancias',*OK)+chip('💳 Fianza activa · 3 cobradas',*OK)+'</div>')
    sug=('<div style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center"><span style="font-size: 13px; font-weight: 700; margin-right: 4px">Vende más:</span>'+''.join('<button type="button" data-connect style="padding: 7px 11px; border: 1.5px solid #385BF8; border-radius: 999px; background: #FFFFFF; color: #385BF8; font-size: 12px; font-weight: 700; font-family: inherit; cursor: pointer">+ %s</button>'%t for t in ['Traslado al aeropuerto','Limpieza extra','Pack de bienvenida']))+'</div>'
    head=sec('Ventas extra','<a href="#" style="font-size: 13px; font-weight: 700; text-decoration: none">Ver tus 4 ofertas →</a>')
    body=(roi+mini+chart) if mob_ else (roi+'<div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 18px; align-items: end">'+mini+chart+'</div>')
    up=card(head+body+protf+sug+'<div style="font-size: 11px; color: #9696B9">Datos y precio de suscripción de ejemplo.</div>',18,' class="stepin"')
    if mob_: return hero+tiles+falta+res+legal+viv+up
    return hero+tiles+'<div style="display: grid; grid-template-columns: 1.7fr 1fr; gap: 14px; align-items: start">'+res+'<div style="display: flex; flex-direction: column; gap: 14px">'+falta+legal+'</div></div>'+viv+up
W(M('Panel'),HEAD.replace('Vivienda 2','Inicio')+'<div style="width: 390px; min-height: 824px; box-sizing: border-box; padding: 16px 20px 24px; display: flex; flex-direction: column; gap: 14px; background: #F7F7FC; %s"><div style="display: flex; justify-content: space-between; align-items: center">%s<span style="padding: 6px 10px; border-radius: 999px; background: #EFEFFF; font-size: 12px; font-weight: 700">Prueba · 14&nbsp;días</span></div>%s</div>\n'%(FONT,LOGO_M,panel(True))+FOOT_m)
W(P('Panel'),HEAD.replace('Vivienda 2','Inicio · portátil')+'<div class="fx" style="width: 1440px; height: 900px; box-sizing: border-box; display: flex; background: #F7F7FC; %s">%s<main style="flex-grow: 1; min-width: 0; height: 900px; overflow-y: auto; box-sizing: border-box; padding: 28px 48px"><div style="max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px">%s</div></main></div>\n'%(FONT,APPNAV,panel(False))+FOOT_p)
print('ok')

# ================= MISMO MARCO PARA TODO =================
INP='height: 48px; border-radius: 12px; border: 1.5px solid #DEDEEB; padding: 0 14px; font-size: 16px; font-family: inherit; color: #19194B; background: #FFFFFF; box-sizing: border-box; width: 100%'
PB='display: block; width: 100%; box-sizing: border-box; height: 50px; line-height: 50px; border: 0; border-radius: 12px; background: #385BF8; color: #FFFFFF; font-size: 16px; font-weight: 700; text-align: center; text-decoration: none; font-family: inherit; cursor: pointer; box-shadow: 0 6px 16px rgba(56, 91, 248, 0.28)'
SB='display: block; width: 100%; box-sizing: border-box; height: 48px; line-height: 44px; border: 2px solid #C9CBEA; border-radius: 12px; background: #FFFFFF; color: #19194B; font-size: 15px; font-weight: 700; text-align: center; text-decoration: none; font-family: inherit; cursor: pointer'
def ok(t): return '<div class="stepin" style="display: flex; gap: 10px; align-items: center; padding: 10px 14px; border-radius: 12px; background: #E8F6EF; color: #0F5C3B; font-size: 14px; line-height: 1.4; font-weight: 600"><span aria-hidden="true">✓</span><span>%s</span></div>'%t
def lab(i,t): return '<label for="%s" style="font-size: 14px; font-weight: 600">%s</label>'%(i,t)
def H(t,sub,size=28): return '<div class="stepin" style="display: flex; flex-direction: column; gap: 8px"><h1 style="margin: 0; font-size: %dpx; line-height: 1.2; font-weight: 800; letter-spacing: -0.01em">%s</h1><p style="margin: 0; font-size: 15px; line-height: 1.5; color: #6B6B95">%s</p></div>'%(size,t,sub)
G='<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" style="vertical-align: -4px; margin-right: 8px"><path d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z" fill="#4285F4"></path><path d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z" fill="#34A853"></path><path d="M6.4 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.4H3.1a10 10 0 0 0 0 9.2L6.4 14z" fill="#FBBC05"></path><path d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.9-2.9A10 10 0 0 0 3.1 7.4L6.4 10c.8-2.4 3-4.1 5.6-4.1z" fill="#EA4335"></path></svg>'
def otp(go,k):
    return '<div data-otp-go="%s" style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px">'%go+''.join('<input%s aria-label="Dígito %d" maxlength="1" inputmode="numeric" style="height: 54px; border-radius: 12px; border: 1.5px solid #DEDEEB; text-align: center; font-size: 22px; font-weight: 800; font-family: inherit; color: #19194B; background: #FFFFFF; min-width: 0">'%((' id="%s"'%k) if i==1 else '',i) for i in range(1,7))+'</div>'
def entrar_form(P,k):
    demo=('<div class="stepin" style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center; justify-content: center; padding: 8px; border-radius: 12px; border: 1px dashed #C9CBEA; font-size: 12px; color: #6B6B95">Demo · Chekin reconoce el email:'
      '<button type="button" data-set="datos" style="padding: 6px 10px; border: 0; border-radius: 999px; background: #EFEFFF; color: #19194B; font-size: 12px; font-weight: 700; font-family: inherit; cursor: pointer">Cliente nuevo</button>'
      '<button type="button" data-set="login" style="padding: 6px 10px; border: 0; border-radius: 999px; background: #EFEFFF; color: #19194B; font-size: 12px; font-weight: 700; font-family: inherit; cursor: pointer">Ya tiene cuenta</button></div>')
    inicio=('<div data-st="inicio" class="stepin" style="display: flex; flex-direction: column; gap: 12px">'
      '<div style="text-align: right; font-size: 14px">¿Ya eres cliente? <button type="button" data-set="login" style="border: 0; background: none; padding: 8px 4px; color: #385BF8; font-size: 14px; font-weight: 800; font-family: inherit; cursor: pointer">Entrar →</button></div>'
      '<a href="%s" style="%s">%sContinuar con Google</a>'%(P('Negocio'),SB.replace('line-height: 44px','line-height: 44px'),G)
      +'<div style="display: flex; align-items: center; gap: 10px; font-size: 12px; font-weight: 700; letter-spacing: 0.06em; color: #9696B9"><span style="flex-grow: 1; height: 1px; background: #E6E6F2"></span>O CON TU EMAIL<span style="flex-grow: 1; height: 1px; background: #E6E6F2"></span></div>'
      +lab(k+'em','Tu email')+'<input id="%sem" type="email" placeholder="tu@email.com" style="%s">'%(k,INP)
      +'<button type="button" data-set="datos" style="%s">Continuar</button>'%PB
      +'<div style="font-size: 13px; line-height: 1.45; color: #55557F; text-align: center">Al continuar, con Google o con tu email, aceptas las <a href="#" style="font-weight: 700">Condiciones</a> y la <a href="#" style="font-weight: 700">Política de privacidad</a> de Chekin.</div>'+'<div style="font-size: 13px; line-height: 1.45; color: #6B6B95; text-align: center">¿Ya tienes cuenta? Usa tu email de siempre: te reconocemos y entras directo. Sin contraseñas.</div>'+demo+'</div>')
    datos=('<div data-st="datos" hidden style="display: flex; flex-direction: column; gap: 12px">'+ok('¡Te damos la bienvenida a Chekin! ¿Cómo te llamas?')
      +'<div class="stepin" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px"><div style="display: flex; flex-direction: column; gap: 6px">'+lab(k+'nm','Nombre')+'<input id="%snm" placeholder="Katia" style="%s"></div>'%(k,INP)
      +'<div style="display: flex; flex-direction: column; gap: 6px">'+lab(k+'ap','Apellidos')+'<input id="%sap" placeholder="Ruiz" style="%s"></div></div>'%(k,INP)
      +'<label class="stepin" style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px; line-height: 1.45; cursor: pointer"><input type="checkbox" style="width: 22px; height: 22px; margin: 0; flex-shrink: 0; accent-color: #385BF8">Quiero recibir consejos y novedades de Chekin por email (opcional).</label>'
      +'<button type="button" data-set="codigo" class="stepin" style="%s">Crear mi cuenta</button>'%PB
      +'<button type="button" data-set="inicio" style="border: 0; background: none; color: #385BF8; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer; padding: 8px">Usar otro email</button></div>')
    codigo=('<div data-st="codigo" hidden data-errbox style="display: flex; flex-direction: column; gap: 12px">'+ok('Te hemos enviado un código de 6 dígitos a katia@email.com')
      +'<div class="stepin" style="display: flex; flex-direction: column; gap: 8px">'+lab(k+'c1','Código de 6 dígitos')+otp('negocio',k+'c1')+'<div style="font-size: 13px; color: #6B6B95">Al escribir el último dígito, entras. ¿No te ha llegado? <a href="#" style="font-weight: 700">Te lo enviamos otra vez</a></div>'+errbox('Ese código no es correcto o ha caducado. Te hemos enviado uno nuevo.','Demo: código incorrecto')+'</div></div>')
    login=('<div data-st="login" hidden style="display: flex; flex-direction: column; gap: 12px">'+ok('¡Hola de nuevo, Katia! Te hemos enviado un código a katia@email.com')
      +'<div class="stepin" style="display: flex; flex-direction: column; gap: 8px">'+lab(k+'l1','Código de acceso')+otp('panel',k+'l1')+'<div style="font-size: 13px; color: #6B6B95">Al escribir el último dígito vuelves a tu panel, donde lo dejaste. Sin contraseñas.</div></div></div>')
    return inicio+datos+codigo+login

def negocio(P,k,mob):
    tipos=''.join('<button type="button" class="chip%s" data-group="tipo" data-val="%s" style="height: 52px; font-size: 14px">%s</button>'%(' on' if i==0 else '',v,l) for i,(v,l) in enumerate([('vr','Alquiler vacacional'),('hotel','Hotel o aparthotel'),('camping','Camping'),('otro','Otro')]))
    sb='height: 52px; width: 52px; flex-shrink: 0; border-radius: 12px; border: 1.5px solid #DEDEEB; background: #FFFFFF; color: #19194B; font-size: 22px; font-weight: 700; font-family: inherit; cursor: pointer'
    stepper=('<div style="display: flex; flex-direction: column; gap: 8px">'+lab(k+'uds','¿Cuántas <span class="unidad">viviendas</span> gestionas?')
      +'<div data-stepper style="display: flex; gap: 8px; align-items: center; max-width: 230px"><button type="button" data-step="-1" aria-label="Restar una" style="%s">−</button><input id="%suds" data-uds type="number" min="1" inputmode="numeric" placeholder="0" style="flex-grow: 1; min-width: 0; height: 52px; border-radius: 12px; border: 1.5px solid #DEDEEB; text-align: center; font-size: 18px; font-weight: 800; font-family: inherit; color: #19194B; background: #FFFFFF"><button type="button" data-step="1" aria-label="Sumar una" style="%s">+</button></div>'%(sb,k,sb)
      +'<div style="font-size: 12px; color: #6B6B95">El número exacto: así dejamos lista cada una.</div></div>')
    tel=('<div style="display: flex; flex-direction: column; gap: 8px">'+lab(k+'tel','Teléfono <span style="font-weight: 400; color: #6B6B95">(opcional)</span>')
      +'<div style="display: flex; gap: 8px"><select aria-label="Prefijo" style="width: 96px; height: 48px; border-radius: 12px; border: 1.5px solid #DEDEEB; background: #FFFFFF; font-size: 15px; font-weight: 700; font-family: inherit; color: #19194B; padding: 0 8px"><option>🇪🇸 +34</option><option>🇮🇹 +39</option><option>🇵🇹 +351</option><option>🇫🇷 +33</option><option>🇩🇪 +49</option><option>🇬🇧 +44</option></select><input id="%stel" type="tel" placeholder="600 000 000" style="%s; flex-grow: 1; min-width: 0; width: auto"></div>'%(k,INP)
      +'<p data-expert-ok hidden style="margin: 0; padding: 10px 12px; border-radius: 12px; background: #E8F6EF; color: #0F5C3B; font-size: 13px; line-height: 1.45; font-weight: 600">¡Hecho! Ya hemos avisado a un experto en Chekin: te llamará para configurarlo contigo.</p>'
      +'<div style="font-size: 12px; color: #6B6B95">Solo lo usamos para ayudarte con la configuración: sin publicidad y sin cedérselo a nadie. <a href="#" style="font-weight: 700">Privacidad</a></div></div>')
    card=('<div class="stepin" style="display: flex; flex-direction: column; gap: 18px; padding: 20px; border-radius: 18px; background: #FFFFFF; box-shadow: %s">'%SH
      +'<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 14px; font-weight: 600">¿Qué gestionas?</div><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">%s</div></div>'%tipos
      +stepper+tel+'</div>')
    btns=('<a href="%s" data-expert-gate class="stepin" style="%s">Entrar en Chekin →</a>'%(P('Creando'),PB)
      +'<a href="%s" data-expert-gate style="display: block; text-align: center; padding: 10px; font-size: 14px; font-weight: 700; color: #385BF8; text-decoration: none">Ahora no</a>'%P('Creando'))
    return ok('Tres datos rápidos · ⏱ 15 s')+H('Cuéntanos tu negocio','Con esto preparamos tu panel a tu medida.',24 if mob else 28)+card+btns
def expert(align,w):
    return ('<div data-expert hidden style="position: absolute; inset: 0; z-index: 5; display: flex; align-items: %s; justify-content: center; background: rgba(25, 25, 75, 0.45)">'
      '<div class="pop" role="dialog" aria-modal="true" aria-label="Ayuda de un experto" style="width: %s; box-sizing: border-box; padding: 26px; border-radius: 20px; background: #FFFFFF; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 20px 60px rgba(25, 25, 75, 0.25)">'
      '<div style="align-self: flex-start; padding: 5px 10px; border-radius: 999px; background: #EFEFFF; color: #385BF8; font-size: 12px; font-weight: 800">Más de <span class="exlim">10</span> <span class="unidad">viviendas</span></div>'
      '<h2 style="margin: 0; font-size: 21px; line-height: 1.3; font-weight: 800">¿Quieres que un experto en Chekin te ayude a configurar tus <span class="unidad">viviendas</span>?</h2>'
      '<p style="margin: 0; font-size: 14px; line-height: 1.5; color: #6B6B95">Con tantas, lo más rápido es hacerlo juntos: las importamos desde tu PMS y dejamos listos el parte de viajeros y el check-in online. Mientras, ya puedes entrar.</p>'
      '<button type="button" data-expert-yes style="%s">Sí, que me contacte un experto</button>'
      '<p style="margin: 0; font-size: 13px; line-height: 1.45; color: #55557F; text-align: center">Te contactaremos solo para configurar Chekin contigo, al teléfono que nos des o por email.</p>'
      '<button type="button" data-expert-no style="border: 0; background: none; color: #385BF8; font-size: 14px; font-weight: 700; font-family: inherit; cursor: pointer; padding: 8px">Prefiero hacerlo yo</button>'
      '</div></div>')%(align,w,PB)

CHP=['Prueba gratis 14 días']
head_e=H('Prueba Chekin gratis 14&nbsp;días','Sin tarjeta de crédito y sin permanencia. Entra en un minuto.')
trust='<div class="stepin" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 14px; font-size: 12px; color: #6B6B95"><span>🔒 Cumplimos el RGPD</span><span>+200.000 propiedades y +25M de check-ins</span></div>'
W(M('Main'),mob('Entrar',0,head_e.replace('font-size: 28px','font-size: 24px')+entrar_form(M,'m')+trust,''))
W(P('Main').replace('Main','Entrar'),lap('Entrar',0,CHP,head_e+card(entrar_form(P,'p'),22)+trust,'',''))
W(M('Negocio'),mob('Tu negocio',0,negocio(M,'m',True),'','',expert('flex-end','100%')))
W(P('Negocio'),lap('Tu negocio',0,CHP+['Katia'],negocio(P,'p',False),'','',extra=expert('center','480px')))
crea2=crea.replace('padding: 40px 24px','padding: 40px 0')
W(M('Creando'),mob('Creando tu cuenta',0,crea2,''))
W(P('Creando'),lap('Creando tu cuenta',0,CHP+['Katia','4 viviendas'],crea2.replace('href="Bienvenida.dc.html"','href="Portatil-Bienvenida.dc.html"'),'',''))
def appnav():
    items=['Inicio','Reservas','Viviendas','Bandeja de entrada','Upselling','Cumplimiento legal','Documentos']
    li=''.join('<div style="padding: 10px 12px; border-radius: 10px; font-size: 14px; %s">%s</div>'%('background: rgba(255, 255, 255, 0.1); color: #FFFFFF; font-weight: 700' if i==0 else 'color: #C9CBEA',n) for i,n in enumerate(items))
    return ('<aside style="width: 300px; flex-shrink: 0; box-sizing: border-box; padding: 30px 26px; display: flex; flex-direction: column; gap: 22px; background: linear-gradient(180deg, #161643, #1F1F57); color: #FFFFFF">'+LOGO_W
      +'<nav aria-label="Menú" style="display: flex; flex-direction: column; gap: 4px">'+li+'</nav><div style="margin-top: auto; font-size: 13px; color: #C9CBEA">Plan y facturación</div></aside>')
W(P('Panel'),HEAD.replace('Vivienda 2','Inicio · portátil')+'<div class="fx" style="position: relative; width: 1440px; height: 900px; box-sizing: border-box; display: flex; background: #F7F7FC; %s">%s<main style="flex-grow: 1; min-width: 0; height: 900px; overflow-y: auto; box-sizing: border-box; padding: 28px 56px"><div style="max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px">%s</div></main></div>\n'%(FONT,appnav(),panel(False))+FOOT_p)
print('ok')

# ---------- Inicio de una cuenta nueva (honesto) ----------
def panel_nuevo(mob_):
    def chip(t,c,bg): return '<span style="display: inline-block; padding: 3px 8px; border-radius: 999px; background: %s; color: %s; font-size: 12px; font-weight: 700; white-space: nowrap">%s</span>'%(bg,c,t)
    hero=('<section class="stepin" style="display: flex; flex-direction: column; gap: 6px; padding: 20px 22px; border-radius: 20px; background: linear-gradient(135deg, #19194B, #2E3B9E); color: #FFFFFF">'
      '<div style="font-size: 12px; color: #C9CBEA">Prueba gratis · quedan 14 días · sin tarjeta</div><h1 style="margin: 0; font-size: %dpx; font-weight: 800">Tu panel, Katia</h1>'
      '<div style="font-size: 14px; color: #DCE3FF">Aquí verás tus llegadas, tus huéspedes y lo que falta. Ahora, lo primero:</div></section>')%(22 if mob_ else 26)
    T=[('legal','🛡️','Conectar el parte de viajeros','Sin él no se puede enviar el check-in a tus huéspedes','3 min',PP('Legal'),'Conectar'),
       ('viv','🏠','Añadir tus viviendas','Solo nombre y dirección, una a una','30 s cada una',PP('Vivienda'),'Añadir'),
       ('res','📅','Recibir tu primera reserva','Conecta tu calendario o crea una a mano','2 min',PP('Reservas'),'Empezar')]
    rows=''.join('<div data-task="%s" style="display: flex; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid #F0F0F7"><span style="font-size: 20px">%s</span><div style="flex-grow: 1; min-width: 0"><div style="font-size: 15px; font-weight: 700">%s</div><div style="font-size: 13px; color: #55557F">%s · ⏱ %s</div></div><a href="%s" style="flex-shrink: 0; padding: 9px 14px; border-radius: 10px; background: #385BF8; color: #FFFFFF; font-size: 14px; font-weight: 700; text-decoration: none">%s</a></div>'%t for t in T)
    tasks=card('<div style="display: flex; justify-content: space-between; align-items: baseline"><h2 style="margin: 0; font-size: 18px; font-weight: 800">Lo que te queda</h2><span data-tasks-n style="font-size: 13px; color: #55557F">3 tareas</span></div>'+rows+'<div data-tasks-done hidden style="font-size: 14px; color: #0F7B4F; font-weight: 700">✓ Todo configurado. ¡A recibir huéspedes!</div>',18,' class="stepin"')
    empty=card('<h2 style="margin: 0; font-size: 18px; font-weight: 800">Próximas reservas</h2><div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 18px 10px; text-align: center"><div style="font-size: 30px">🗓️</div><div style="font-size: 15px; font-weight: 700">Aún no tienes reservas</div><div style="font-size: 13px; color: #55557F">Cuando llegue la primera, la verás aquí con su check-in y su parte.</div><a href="%s" style="margin-top: 4px; padding: 10px 16px; border-radius: 12px; border: 2px solid #C9CBEA; color: #19194B; font-size: 14px; font-weight: 700; text-decoration: none">Crear una reserva de prueba</a></div>'%PP('Reservas'),18,' class="stepin"')
    extras=card('<h2 style="margin: 0; font-size: 18px; font-weight: 800">Ventas extra</h2><div style="font-size: 14px; line-height: 1.5; color: #55557F">Las que actives salen en el check-in de cada huésped. Lo que vendan, menos la comisión de Chekin, te ayuda a pagar tu plan: lo verás aquí cada mes. <a href="#" style="font-weight: 700">Comisiones</a></div><div style="display: flex; flex-wrap: wrap; gap: 8px">'+'<span data-pn="prot">'+chip('🛡️ Protección y fianza',*('#0F5C3B','#E8F6EF'))+'</span><span data-pn="ven">'+chip('🌙 4 ofertas listas',*('#385BF8','#EFEFFF'))+'</span>'+'</div>',18,' class="stepin"')
    trial=card('<h2 style="margin: 0; font-size: 18px; font-weight: 800">Tu prueba gratis</h2><div style="font-size: 14px; line-height: 1.5; color: #55557F">Quedan <b style="color: #19194B">14 días</b> (hasta el 17 de noviembre). Sin tarjeta y sin permanencia.</div><div style="display: flex; justify-content: space-between; align-items: baseline; gap: 10px; padding: 12px 14px; border-radius: 12px; background: #F4F6FF"><span style="font-size: 14px">Después, tu plan</span><span><b style="font-size: 18px">%d €/mes</b> <span style="font-size: 12px; color: #55557F">(ejemplo)</span></span></div><a href="#" style="font-size: 14px; font-weight: 700; text-decoration: none">Ver planes y precios →</a>'%PLAN_EJ,18,' class="stepin"')
    preview='<a href="%s" class="stepin" style="align-self: center; padding: 10px; font-size: 14px; font-weight: 700; text-decoration: none">Así se verá tu Inicio con reservas →</a>'%PP('Panel')
    if mob_: return hero+tasks+empty+extras+trial+preview
    return hero+'<div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 14px; align-items: start"><div style="display: flex; flex-direction: column; gap: 14px">'+tasks+empty+'</div><div style="display: flex; flex-direction: column; gap: 14px">'+extras+trial+'</div></div>'+preview
PP=M
W(M('PanelNuevo'),HEAD.replace('Vivienda 2','Inicio (cuenta nueva)')+'<div style="width: 390px; min-height: 824px; box-sizing: border-box; padding: 16px 20px 24px; display: flex; flex-direction: column; gap: 14px; background: #F7F7FC; %s"><div style="display: flex; justify-content: space-between; align-items: center">%s<span style="padding: 6px 10px; border-radius: 999px; background: #EFEFFF; font-size: 12px; font-weight: 700">Prueba · 14&nbsp;días</span></div>%s</div>\n'%(FONT,LOGO_M,panel_nuevo(True))+FOOT_m)
PP=P
W(P('PanelNuevo'),HEAD.replace('Vivienda 2','Inicio (cuenta nueva) · portátil')+'<div class="fx" style="position: relative; width: 1440px; height: 900px; box-sizing: border-box; display: flex; background: #F7F7FC; %s">%s<main style="flex-grow: 1; min-width: 0; height: 900px; overflow-y: auto; box-sizing: border-box; padding: 28px 56px"><div style="max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px">%s</div></main></div>\n'%(FONT,appnav(),panel_nuevo(False))+FOOT_p)
print('panel nuevo ok')
