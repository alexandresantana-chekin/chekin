import re,sys
SRC="tools/sales-card/decks/hotels-en-original-for-italian.html"
DST="sales-card/presentaciones/hotels-it.html"
s=open(SRC,encoding="utf-8").read()
TX={
'Chekin presentation for Hotels':'Presentazione di Chekin per gli hotel',
'Book a demo':'Prenota una demo',
'Trusted by 10,000+ hotels worldwide':'Scelta da oltre 10.000 hotel in tutto il mondo',
'The all-in-one guest experience platform for ':"La piattaforma all-in-one per l'esperienza degli ospiti negli ",
'modern hotels':'hotel moderni',
'From online check-in to check-out: ID verification, digital keys, legal compliance, upselling and guest messaging, managed from one dashboard.':"Dal check-in online al check-out: verifica dell'identità, chiavi digitali, conformità legale, upselling e messaggistica con gli ospiti, tutto da un unico pannello.",
'hotels worldwide':'hotel nel mondo','guest check-ins':'check-in di ospiti','countries covered':'paesi coperti','integrations':'integrazioni',
'Take the 2-min tour ':'Fai il tour di 2 min ',
"Today's arrivals":'Arrivi di oggi','Hotel Marbella · Fri 14 Nov':'Hotel Marbella · ven 14 nov',
'Arrivals':'Arrivi','Online':'Online','ID verified':'ID verificati','Upsells':'Upsell',
'2 guests · 2 nights':'2 ospiti · 2 notti','Verified':'Verificato','Paid':'Pagato','Key sent':'Chiave inviata',
'1 guest · 3 nights':'1 ospite · 3 notti','Upgrade +€35':'Upgrade +35 €','3 guests · 4 nights':'3 ospiti · 4 notti','Report sent':'Comunicazione inviata','Arriving 23:40':'Arriva alle 23:40',
'2 guests · 1 night':'2 ospiti · 1 notte','Tourist tax paid':'Tassa di soggiorno pagata','Late check-out':'Late check-out',
'What changed':'Cosa è cambiato','The stay no longer begins ':'Il soggiorno non inizia più ','at the front desk':'alla reception',
'Guests arrive with app-like expectations, while hotels run on tighter margins and face more regulation every year.':"Gli ospiti arrivano con aspettative da app, mentre gli hotel lavorano con margini più stretti e più normative ogni anno.",
'Without Chekin':'Senza Chekin','With Chekin':'Con Chekin','Guests expect app-like speed':"Gli ospiti si aspettano la rapidità di un'app",
'10 min':'10 min','for a traditional check-in at the desk, often with a queue.':'per un check-in tradizionale alla reception, spesso con la coda.',
'1 min':'1 min','Paperless check-in from their phone, at any hour, in their own language.':'Check-in senza carta dal cellulare, a qualsiasi ora e nella propria lingua.',
'Teams are stretched':'I team sono al limite','30+ h':'30+ h','a month that many hotel teams spend on admin paperwork.':'al mese che molti team alberghieri dedicano alla burocrazia.',
'time at the front desk, so staff can focus on welcoming guests.':'di tempo alla reception, così il personale si concentra sull’accoglienza.',
'Compliance keeps growing':'Le normative continuano a crescere','15+':'15+','countries with their own guest-report, tourist-tax and e-invoicing rules.':'paesi con regole proprie su comunicazione degli ospiti, tassa di soggiorno e fatturazione elettronica.',
'24 h':'24 h','Guest reports sent to the authorities automatically after check-in.':'Comunicazioni degli ospiti inviate automaticamente alle autorità dopo il check-in.',
'Online check-in · Identity verification':"Check-in online · Verifica dell'identità",'Guests arrive ':'Gli ospiti arrivano ','registered, verified and paid':'registrati, verificati e già pagati',
'Pre-arrival registration':"Registrazione prima dell'arrivo"," from any phone, branded with your hotel's logo and colours.":' da qualsiasi cellulare, con il logo e i colori del tuo hotel.',
'Passport or ID scan:':'Scansione di passaporto o carta d’identità:',' OCR fills in the form and the MRZ is cross-checked against it.':' l’OCR compila il modulo e viene confrontato con la MRZ.',
'Biometric selfie and liveness check':'Selfie biometrico e prova di vita',' confirm the guest is the document holder.':' confermano che l’ospite è il titolare del documento.',
'Tourist tax and balance':'Tassa di soggiorno e saldo',' settled before the guest reaches the desk.':' regolati prima che l’ospite arrivi alla reception.',
'10 ':'10 ',' 1 min':' 1 min','check-in at the desk':'check-in alla reception',"countries' documents":'documenti di paesi','document templates':'modelli di documento',
'Tap ':'Tocca ','Finish check-in':'Termina il check-in',' on the phone.':' sul cellulare.',
'Welcome, Marta':'Benvenuta, Marta','Fri 14 – Sun 16 Nov · Deluxe double':'ven 14 – dom 16 nov · Doppia deluxe',
'Guest details':'Dati degli ospiti','2 of 2 guests':'2 ospiti su 2','Passport · MRZ':'Passaporto · MRZ','Read by OCR, MRZ match':'Letto con OCR, MRZ corrispondente',
'Selfie · liveness':'Selfie · prova di vita','Face match 99.4%':'Corrispondenza del volto 99,4 %','Balance + tourist tax':'Saldo + tassa di soggiorno','€342.00 + €8.00':'342,00 € + 8,00 €',
'Arrival time':'Ora di arrivo','Around 23:40':'Verso le 23:40','RECEPTION VIEW':'VISTA RECEPTION','Room 214 · arriving 23:40':'Camera 214 · arriva alle 23:40',
'Pending':'In sospeso','Registration':'Registrazione','0/2 guests':'0/2 ospiti','Identity':'Identità','Balance':'Saldo','€350.00 due':'350,00 € da pagare','Guest report':'Comunicazione ospiti','Digital key':'Chiave digitale',
'Onsite check-in · Kiosks · Digital keys':'Check-in in hotel · Totem · Chiavi digitali','Walk-ins in under a minute. ':'Clienti senza prenotazione in meno di un minuto. ','Late arrivals without the desk.':'Arrivi notturni senza reception.',
'Onsite and kiosks':'In hotel e totem','Tablet and kiosk modes':'Modalità tablet e totem','OCR reads the ID in seconds':'L’OCR legge il documento in pochi secondi','Hand-off to staff when needed':'Passaggio al personale quando serve',
'Self check-in and keys':'Self check-in e chiavi','Mobile keys, 20+ lock brands':'Chiavi sul cellulare, oltre 20 marche di serrature','Access valid only for the stay':'Accesso valido solo per il soggiorno','Revoke a key in one click':'Revoca una chiave con un clic',
'Arriving at 23:40? The guest checks in online, gets the key on their phone and goes straight to the room. Try it on the phone.':"Arriva alle 23:40? L'ospite fa il check-in online, riceve la chiave sul cellulare e va direttamente in camera. Provalo sul telefono.",
'Welcome, James':'Benvenuto, James','Fri 15:00 – Sun 11:00':'ven 15:00 – dom 11:00','Room · 1st floor':'Camera · 1º piano','Tap to open room 118':'Tocca per aprire la camera 118',
'Main entrance':'Ingresso principale','24/7 during your stay':'24 ore su 24 durante il soggiorno','Parking garage':'Garage','Level −1':'Livello −1','Valid until Sun 11:00':'Valida fino a dom 11:00','Revoked at check-out':'Revocata al check-out',
'Legal compliance':'Conformità legale','Your team never opens ':'Il tuo team non aprirà più ','a government portal':'un portale della pubblica amministrazione',' again':'',
'Guest reports go to the authorities automatically within 24 hours of check-in. Tourist tax is calculated for you, and e-invoicing is built in.':'Le comunicazioni degli ospiti arrivano alle autorità automaticamente entro 24 ore dal check-in. La tassa di soggiorno è calcolata per te e la fatturazione elettronica è integrata.',
'tourist tax jurisdictions':'giurisdizioni con tassa di soggiorno','automatic submission':'invio automatico','Tap your country:':'Tocca il tuo paese:','Automatic submission to the authorities':'Invio automatico alle autorità','Digital guest book, stored for you':'Registro digitale degli ospiti, archiviato per te',
'Submissions to the authorities · Today':'Invii alle autorità · Oggi','All sent':'Tutto inviato','Portals opened by your team':'Portali aperti dal tuo team',
'Upselling':'Upselling','Earn more ':'Guadagna di più ','without selling a single extra room':'senza vendere una camera in più','Room upgrades':'Upgrade di camera',
' mapped from your PMS room types, plus early check-in, breakfast, parking and spa: offered during online check-in, matched to each guest by AI and paid in the same flow.':' a partire dalle tipologie di camera del tuo PMS, più early check-in, colazione, parcheggio e spa: proposti durante il check-in online, abbinati a ogni ospite dall’IA e pagati nello stesso flusso.',
'Sea view room ':'Camera vista mare ','+€35':'+35 €','Early check-in ':'Early check-in ','+€18':'+18 €','Breakfast ':'Colazione ','+€16':'+16 €','Parking ':'Parcheggio ','+€20':'+20 €','Spa circuit ':'Percorso spa ','+€45':'+45 €',
'attach rate at check-in':'di adesione al check-in','average upsell per booking':'di upsell medio per prenotazione','What could your hotel add?':'Quanto potrebbe aggiungere il tuo hotel?',
'100-room hotel':'Hotel da 100 camere','5-hotel boutique chain · 240 rooms':'Catena boutique di 5 hotel · 240 camere','Estimated monthly uplift':'Incremento mensile stimato',
' a year · ':' all’anno · ',' bookings a month':' prenotazioni al mese','Rooms ':'Camere ','Occupancy ':'Occupazione ','Average stay ':'Soggiorno medio ','2 nights':'2 notti','Guests who add an extra ':'Ospiti che aggiungono un extra ',
'Bookings a month = rooms × 30 × occupancy ÷ average stay, × attach rate × €55 average upsell. An estimate, not a guarantee.':'Prenotazioni al mese = camere × 30 × occupazione ÷ soggiorno medio, × adesione × 55 € di upsell medio. È una stima, non una garanzia.',
'Unified inbox · Check-out':'Inbox unificata · Check-out','Fewer calls to reception. ':'Meno chiamate alla reception. ','A check-out as smooth as the welcome.':'Un check-out fluido come l’accoglienza.',
'AI replies 24/7':'L’IA risponde 24 ore su 24'," on WhatsApp, SMS, email and OTAs, using your property's own information.":' su WhatsApp, SMS, email e OTA, con le informazioni della tua struttura.',
'Digital guidebook':'Guida digitale'," translated automatically into the guest's language.":' tradotta automaticamente nella lingua dell’ospite.',
'Mobile check-out':'Check-out da cellulare',' with folio review and late check-out or transfer add-ons.':' con revisione del conto ed extra come late check-out o transfer.',
'E-invoice and review request':'Fattura elettronica e richiesta di recensione',' sent at the right moment.':' inviate al momento giusto.','more 5★ reviews':'recensioni 5★ in più',
'Room 214 · WhatsApp':'Camera 214 · WhatsApp','Reply or let AI handle it…':'Rispondi o lascia fare all’IA…','↻ Replay conversation':'↻ Rivedi la conversazione',
'Proven outcomes':'Risultati dimostrati','Why hotels ':'Perché gli hotel ','switch to Chekin':'passano a Chekin','time at the front desk':'di tempo alla reception',
'Check-in from 10 minutes to under one':'Check-in da 10 minuti a meno di uno','9–14% of guests add an extra':'Il 9–14 % degli ospiti aggiunge un extra','Less friction, better ratings':'Meno attrito, valutazioni migliori',
'25M+ guest check-ins':'Oltre 25 M di check-in','Guest reports, tourist tax, e-invoicing':'Comunicazioni ospiti, tassa di soggiorno, fatturazione elettronica','PMS, channel managers, locks':'PMS, channel manager, serrature',
'Works with your PMS:':'Funziona con il tuo PMS:','+200 more →':'+200 altri →','We replaced four separate vendors with Chekin.':'Abbiamo sostituito quattro fornitori diversi con Chekin.','Operations Director, European hotel chain':'Direttore operativo, catena alberghiera europea',
'The hotel of the future runs on Chekin':'L’hotel del futuro funziona con Chekin','15 minutes is all it takes to see what your reception could become':'Bastano 15 minuti per vedere cosa può diventare la tua reception',
"We'll walk you through check-in, compliance and upselling with your own PMS and country in mind.":'Ti mostriamo check-in, conformità e upselling pensando al tuo PMS e al tuo paese.',
'Book my 15-min demo':'Prenota la mia demo di 15 min','Try Chekin free':'Prova Chekin gratis','Calculate my uplift':'Calcola il mio incremento','Copy link to share with your team':'Copia il link da condividere con il tuo team',
'Swipe or use ← →':'Scorri o usa ← →','Next':'Avanti','Link copied':'Link copiato',
'EN':'IT','Sophie Martin':'Sophie Martin','← Card':'← Biglietto','Back to the card':'Torna al biglietto',
}
AR={'Slides':'Diapositive','Copy link to share':'Copia il link da condividere','Chekin for hotels':'Chekin per gli hotel','What changed':'Cosa è cambiato','Compare':'Confronta',
'Online check-in and ID verification':"Check-in online e verifica dell'identità",'Onsite check-in and digital keys':'Check-in in hotel e chiavi digitali','Legal compliance':'Conformità legale','Upselling':'Upselling','Examples':'Esempi',
'Unified inbox and check-out':'Inbox unificata e check-out','Proven outcomes':'Risultati dimostrati','5 stars':'5 stelle','Book a demo':'Prenota una demo','Slide navigation':'Navigazione tra le diapositive','Previous slide':'Diapositiva precedente'}
head,rest=s.split("<script",1)
miss=[]
for en,it in TX.items():
    pat=">"+en+"<"
    if pat in head: head=head.replace(pat,">"+it+"<")
    elif en not in("0","+","%","EN"): miss.append(en)
# € detrás de la cifra, miles con punto
for a,b in [('<b>€<i style="font-style:normal" data-count="1240">0</i></b>','<b><i style="font-style:normal" data-count="1240">0</i> €</b>'),
  ('<em>+</em>€55','<em>+</em>55 €'),('<em>+</em>€<span id="cMonth">5,198</span>','<em>+</em><span id="cMonth">5198</span> €'),
  ('≈ €<span id="cYear">62,370</span> a year · <span id="cBook">1,050</span>','≈ <span id="cYear">62.370</span> € all’anno · <span id="cBook">1050</span>'),
  ('+€<span data-count="55">0</span>','+<span data-count="55">0</span> €')]:
    if a not in head:
        a2=a.replace(" a year · "," all’anno · ")
        if a2 in head: a=a2
        else: miss.append("EUR:"+a[:50]);continue
    head=head.replace(a,b)
head=re.sub(r'(class="pill solid"[^>]*>)Prenota una demo<',r'\1Prenota demo<',head)
for en,it in AR.items(): head=head.replace('aria-label="%s"'%en,'aria-label="%s"'%it)
for v,it in {'Done':'Fatto','Match':'Corrisponde','Paid':'Pagato','Shared':'Condiviso','Verified':'Verificato'}.items():
    head=head.replace('data-s="%s"'%v,'data-s="%s"'%it)
head=head.replace('<title>Chekin presentation for Hotels','<title>Presentazione di Chekin per gli hotel').replace('<html>','<html lang="it">')
js="<script"+rest
J=[
("var LANG='en'","var LANG='it'"),
("document.getElementById('nextTxt').textContent = i===N-1 ? 'Start again' : 'Next';","document.getElementById('nextTxt').textContent = i===N-1 ? 'Ricomincia' : 'Avanti';"),
("'Slide '+(i+1)+': '","'Diapositiva '+(i+1)+': '"),
("showToast('Link copied')","showToast('Link copiato')"),
("toLocaleString('en-US')","toLocaleString('it-IT')"),
("s==='Shared'?'b-blue'","s==='Condiviso'?'b-blue'"),
("<span class=\"badge b-ok\">Checked in</span><span class=\"badge b-ok\">Paid</span><span class=\"badge b-warn\">Late arrival</span>","<span class=\"badge b-ok\">Check-in fatto</span><span class=\"badge b-ok\">Pagato</span><span class=\"badge b-warn\">Arrivo notturno</span>"),
("'<span class=\"badge b-wait\">Pending</span>'","'<span class=\"badge b-wait\">In sospeso</span>'"),
("done?'2/2 guests':'0/2 guests'","done?'2/2 ospiti':'0/2 ospiti'"),
("done?'Verified':'—'","done?'Verificato':'—'"),
("done?'€0.00 due':'€350.00 due'","done?'0,00 € da pagare':'350,00 € da pagare'"),
("done?'Sent':'—'","done?'Inviata':'—'"),
("done?'Ready':'—'","done?'Pronta':'—'"),
("ciBtn.textContent='Finish check-in'","ciBtn.textContent='Termina il check-in'"),
("'✓ Checked in · see you at 23:40'","'✓ Check-in fatto · ti aspettiamo alle 23:40'"),
("'Tap to open room 118'","'Tocca per aprire la camera 118'"),
("'Room 118 unlocked · welcome!'","'Camera 118 aperta · benvenuto!'"),
("['Czech Republic','a']","['Cechia','a']"),("['UAE (Dubai)','a']","['EAU (Dubai)','a']"),("['Brazil','a']","['Brasile','a']"),("['Greece','a']","['Grecia','a']"),("['France','g']","['Francia','g']"),("['United Kingdom','g']","['Regno Unito','g']"),("['Netherlands','g']","['Paesi Bassi','g']"),("['Belgium','g']","['Belgio','g']"),("['Romania','g']","['Romania','g']"),
("['Spain','a',['#C60B1E'","['Spagna','a',['#C60B1E'"),("['Italy','a',['#009246'","['Italia','a',['#009246'"),("['Germany','a'","['Germania','a'"),("['Croatia','a'","['Croazia','a'"),("['Switzerland','a']","['Svizzera','a']"),
("['Spain','Spain · SES.Hospedajes','14 guest reports','Sent']","['Spagna','Spagna · SES.Hospedajes','14 comunicazioni ospiti','Sent']"),
("['Italy','Italy · Alloggiati Web','9 guest reports','Sent']","['Italia','Italia · Alloggiati Web','9 comunicazioni ospiti','Sent']"),
("['Italy','Italy · ISTAT','Occupancy statistics','Sent']","['Italia','Italia · ISTAT','Statistiche sulle presenze','Sent']"),
("['Portugal','Portugal · SIBA','6 guest reports','Sent']","['Portugal','Portogallo · SIBA','6 comunicazioni ospiti','Sent']"),
("['Spain','Tourist tax · Catalonia','€72.00 collected at check-in','Automatic']","['Spagna','Tassa di soggiorno · Catalogna','72,00 € incassati al check-in','Automatic']"),
("['Croatia','Croatia · eVisitor','4 guest reports','Sent']","['Croazia','Croazia · eVisitor','4 comunicazioni ospiti','Sent']"),
("(g?'Digital guest book':'Guest reports')","(g?'Registro digitale degli ospiti':'Comunicazioni ospiti')"),
("g?'Stored for you, ready for inspection':'Sent automatically within 24 h', g?'Stored':'Sent']","g?'Archiviato per te, pronto per i controlli':'Inviato automaticamente entro 24 h', g?'Stored':'Sent']"),
("'<span class=\"badge b-wait\">Sending…</span>'","'<span class=\"badge b-wait\">Invio…</span>'"),
("'<span class=\"badge b-warn\">Automatic</span>':'<span class=\"badge b-ok\">'+r[3]+'</span>'","'<span class=\"badge b-warn\">Automatico</span>':'<span class=\"badge b-ok\">'+LBL[r[3]]+'</span>'"),
("el.innerHTML=v==='Automatic'?'<span class=\"badge b-warn\">Automatic</span>':'<span class=\"badge b-ok\">'+v+'</span>';","el.innerHTML=v==='Automatic'?'<span class=\"badge b-warn\">Automatico</span>':'<span class=\"badge b-ok\">'+LBL[v]+'</span>';"),
("var R=[","var LBL={Sent:'Inviato',Stored:'Archiviato',Automatic:'Automatico'};\n  var R=["),
("stay+(stay===1?' night':' nights')","stay+(stay===1?' notte':' notti')"),
("['g',\"Hi! What's the Wi-Fi password?\"]","['g',\"Salve! Qual è la password del Wi-Fi?\"]"),
("['a','Hi Sophie! The network is \"Marbella_Guest\" and the password is \"seaview214\". It\\'s also in your digital guide.']","['a','Ciao Sophie! La rete è \"Marbella_Guest\" e la password è \"seaview214\". La trovi anche nella tua guida digitale.']"),
("['g','Could we check out a bit later on Sunday?']","['g','Possiamo fare il check-out un po\\' più tardi domenica?']"),
("['a',\"Of course! Late check-out until 13:00 is €25. I've added it to your stay.\"]","['a',\"Certo! Il late check-out fino alle 13:00 costa 25 €. L'ho aggiunto al tuo soggiorno.\"]"),
("'<span class=\"badge b-ok\">AI reply</span>'","'<span class=\"badge b-ok\">Risposta dell’IA</span>'"),
("<b>Late check-out · 13:00</b><small style=\"color:var(--paper-mute)\">Added to the folio</small></span><span class=\"badge b-ok\">+€25</span>","<b>Late check-out · 13:00</b><small style=\"color:var(--paper-mute)\">Aggiunto al conto</small></span><span class=\"badge b-ok\">+25 €</span>"),
]
for a,b in J:
    if a not in js: miss.append("JS:"+a[:60])
    js=js.replace(a,b)
open(DST,"w",encoding="utf-8").write(head+js)
print("faltan:",miss)
