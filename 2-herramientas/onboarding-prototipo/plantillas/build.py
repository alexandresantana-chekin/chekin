import re,sys,os
P=sys.argv[1]; OUT=sys.argv[2]
LOGO=sys.argv[3]; LOGOW=sys.argv[4]
def svg(path,cls):
    s=open(path).read()
    s=re.sub(r'<\?xml[^>]*>','',s).strip()
    s=s.replace('<svg ','<svg class="%s" role="img" aria-label="Chekin" '%cls,1)
    return s
logo=svg(LOGO,'logo'); logow=svg(LOGOW,'logo')
NAMES={'Main':'entrar','Negocio':'negocio','Creando':'creando','Bienvenida':'bienvenida','Reservas':'reservas','ElegirPms':'elegirpms','Conectar':'conectar','Apikey':'apikey','Calendario':'calendario','Cartera':'cartera','Paises':'paises','Titular':'titular','Vivienda':'vivienda','Legal':'legal','Proteccion':'proteccion','Ventas':'ventas','Envio':'envio','Listo':'listo','PanelNuevo':'panelnuevo','Panel':'panel'}
LABELS=[('entrar','Entrar'),('negocio','Tu negocio'),('creando','Creando cuenta'),('bienvenida','Bienvenida'),('reservas','1 · Reservas'),('elegirpms','PMS: elegir'),('conectar','PMS: conectar'),('apikey','PMS: API key'),('calendario','Calendario'),('cartera','2 · Leído del PMS'),('paises','2 · Países'),('titular','3 · Titular'),('vivienda','3 · Viviendas'),('legal','4 · Parte de viajeros'),('proteccion','5 · Protección'),('ventas','6 · Ventas extra'),('envio','7 · Envío'),('listo','¡Todo listo!'),('panelnuevo','Inicio (cuenta nueva)'),('panel','Inicio (con reservas)')]
def body(f):
    s=open(os.path.join(P,f)).read()
    s=s.split('</helmet>',1)[1].split('</x-dc>',1)[0].strip()
    return s
def conv(s, dev, key):
    # links
    for k,v in NAMES.items():
        s=s.replace('href="%s.dc.html"'%(('Portatil-'+{'Main':'Entrar'}.get(k,k)) if dev=='portatil' else k),'href="#%s"'%v)
    s=re.sub(r'href="Portatil-Entrar\.dc\.html"','href="#entrar"',s)
    # logos
    def rimg(m):
        src=m.group(1); st=m.group(2)
        w=re.search(r'width:\s*([0-9]+)px',st).group(1); h=re.search(r'height:\s*([0-9]+)px',st).group(1)
        mg=re.search(r'margin:\s*([^;"]+)',st)
        style='width:%spx;height:%spx;%s'%(w,h,('margin:%s;'%mg.group(1)) if mg else '')
        l = logow if 'c25beceb' in src else logo
        return l.replace('class="logo"','class="logo" style="%s"'%style,1)
    s=re.sub(r'<img src="(/_blob/[0-9a-f]+)" alt="Chekin" style="([^"]*)">',rimg,s)
    # states
    s=re.sub(r'<sc-if value="\{\{inicio\}\}"[^>]*>','<div data-st="inicio">',s)
    s=re.sub(r'<sc-if value="\{\{datos\}\}"[^>]*>','<div data-st="datos" hidden>',s)
    s=re.sub(r'<sc-if value="\{\{codigo\}\}"[^>]*>','<div data-st="codigo" hidden>',s)
    s=s.replace('</sc-if>','</div>')
    s=s.replace('onClick="{{abrir}}"','data-set="datos"').replace('onClick="{{enviar}}"','data-set="codigo"').replace('onClick="{{volver}}"','data-set="inicio"')
    s=s.replace('{{nombre}}','Katia').replace('{{unidad}}','<span class="unidad">viviendas</span>')
    tipos='\n'.join('<button type="button" class="chip%s" data-group="tipo" data-val="%s">%s</button>'%(' on' if i==0 else '',v,l) for i,(v,l) in enumerate([('vr','Alquiler vacacional'),('hotel','Hotel o aparthotel'),('camping','Camping'),('otro','Otro')]))
    tramos='\n'.join('<button type="button" class="chip%s" data-group="tramo" data-val="%s">%s</button>'%(' on' if i==0 else '',v,v) for i,v in enumerate(['1-3','4-10','11-60','+60']))
    s=re.sub(r'<sc-for list="\{\{tipos\}\}".*?</sc-for>',tipos,s,flags=re.S)
    s=re.sub(r'<sc-for list="\{\{tramos\}\}".*?</sc-for>',tramos,s,flags=re.S)
    assert '{{' not in s and 'sc-' not in s, (key, re.findall(r'\{\{[^}]*\}\}|sc-\w+',s)[:5])
    return s
for dev in ('movil','portatil'):
    files=['Main', 'Negocio', 'Creando', 'Bienvenida', 'Reservas', 'ElegirPms', 'Conectar', 'Apikey', 'Calendario', 'Cartera', 'Paises', 'Titular', 'Vivienda', 'Legal', 'Proteccion', 'Ventas', 'Envio', 'Listo', 'PanelNuevo', 'Panel']
    secs=[]
    for k in files:
        f=('Portatil-'+{'Main':'Entrar'}.get(k,k)+'.dc.html') if dev=='portatil' else k+'.dc.html'
        secs.append('<section class="screen" id="scr-%s" hidden>\n%s\n</section>'%(NAMES[k],conv(body(f),dev,k)))
    tpl=open(os.path.join(os.path.dirname(__file__),'tpl_%s.html'%dev)).read()
    nav='\n'.join('<a class="jump" href="#%s" data-jump="%s">%s</a>'%(t,t,l) for t,l in LABELS)
    out=tpl.replace('<!--NAV-->',nav).replace('<!--SCREENS-->','\n'.join(secs))
    open(os.path.join(OUT,'onboarding-%s.html'%dev),'w').write(out)
    print(dev,len(out))
