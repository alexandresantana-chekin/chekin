# Brief — Landing piloto "Check-in online para hoteles – España"

Fecha: 2026-10-21 · Estado: borrador para revisión · Destino: HubSpot (sin publicar)

## 1. Por qué esta landing
- Hoteles ES gasta 24.815 € en 90 días y sale a 591 €/SQL; la referencia en España (Search Intención) está en 271 €/SQL.
- La landing actual (`landing.chekin.com/chekin-hoteles`) convierte al 0,22% (9 formularios / 4.049 clics), su H1 no repite el anuncio y tiene 12 CTA con 8 textos distintos y 2 enlaces de salida.
- Meta Hoteles no tiene landing: todo va a formulario instantáneo (0 ganados de 18 deals).

## 2. Oferta y público
- **Público:** hoteles y cadenas hoteleras en España (director/a de hotel, jefe/a de recepción, revenue/operaciones). No alquiler vacacional.
- **Oferta:** demo gratuita con un especialista en hoteles.
- **Objetivo único:** pedir demo. Un solo tipo de CTA ("Pide tu demo"), todos apuntan al mismo formulario.

## 3. De dónde viene el tráfico (message match)
| Canal | Qué se puja / segmenta | Promesa del anuncio | H1 de la landing |
|---|---|---|---|
| Google Search Hoteles (reactivar) | software check-in hotel, check-in online hotel, check-in digital hotel, recepción automática hotel | "Check-in Online para Hoteles" · "−80% Tiempo en Recepción" | **Check-in online para hoteles: −80% de tiempo en recepción** |
| Google PMax Competitors | (pendiente de términos de búsqueda) — quitar titulares de alquiler vacacional | Igual que arriba | Igual |
| Meta Hoteles | Público de hoteles | Titular nuevo = H1 | Igual · test A/B contra formulario instantáneo |

Keywords negativas a proponer: alquiler vacacional, apartamento turístico, airbnb, plantilla, gratis/word/pdf, contrato.

## 4. Voz del cliente (de anuncios y landing actual)
- Dolor: "recepción saturada", "huéspedes esperando", "colas", "check-ins manuales", "papeleo", "multas".
- Deseo: "recuperar horas", "huésped entra sin colas", "más ingresos por reserva".
- Pendiente: reseñas, tickets o llamadas de ventas reales para afinar (Wiebe).

## 5. Emoción dominante y objeción principal
- **Emoción:** alivio (menos carga para el equipo de recepción) + control (cumplir sin riesgo).
- **Objeción principal:** "¿Funciona con mi PMS?" → bloque de integraciones justo debajo del hero y en FAQ.
- Objeciones secundarias: "¿Cumple con SES.Hospedajes?", "¿Y los huéspedes que no hacen el check-in online?", "¿Qué pasa con los datos?".

## 6. Cifras oficiales (regla: la más alta disponible)
+10.000 hoteles · +200.000 alojamientos · +200 integraciones PMS · +25M check-ins · −80% tiempo en recepción · 3 min check-in medio · +55 € upselling medio por reserva · España: SES.Hospedajes, Mossos d'Esquadra y Ertzaintza (100% del país), INE (estadística), conservación 3 años.
No usar: Verifactu (beta, fecha a confirmar), caso "cadena de 5 hoteles" (es un cálculo, no un cliente real).

## 7. Estructura de la página
1. **Cabecera mínima:** logo (sin enlace) + botón "Pide tu demo" (ancla al formulario). Sin menú.
2. **Hero:** etiqueta "Para hoteles en España" · H1 · subtítulo · 3 viñetas de beneficio · línea de confianza · **formulario a la derecha** (arriba del pliegue).
3. **Integraciones PMS:** "Conectado con el PMS que ya usas" + logos en gris.
4. **Cifras:** −80% · 3 min · +55 € · +10.000 hoteles.
5. **Beneficios (rejilla 3×2):** check-in online, verificación de identidad, parte de viajeros automático, quiosco en el lobby, llegadas tarde con llave digital, upselling en el check-in.
6. **Cómo funciona (3 pasos)** + una sola imagen de producto.
7. **Testimonio de hotel** — PENDIENTE (no inventamos; hace falta uno real).
8. **FAQ** que responde objeciones.
9. **Cierre:** banda azul con CTA repetido.
10. **Footer legal mínimo:** © Chekin · Privacidad · Cookies.

## 8. Formulario (HubSpot, incrustado)
Campos visibles (4): Nombre · Email de trabajo · Teléfono · Número de habitaciones (desplegable: 1–20, 21–50, 51–150, +150).
Ocultos: utm_source, utm_medium, utm_campaign, utm_term, utm_content, gclid/fbclid, landing = "hoteles-es-checkin".
Habitaciones cualifica y permite a ventas priorizar (buscamos SQL, no solo volumen).
Texto del botón: "Pide tu demo". Debajo: "Te contactamos en menos de 24 h laborables" (PENDIENTE confirmar con ventas). Duración de la demo: no se indica hasta confirmarla.

## 9. Hipótesis y medición
- **Hipótesis:** si el H1 repite la promesa del anuncio, hay un solo CTA y el formulario está arriba del pliegue, la conversión clic→formulario sube del 0,22% a ≥3% y el coste por SQL baja de 818 € a <400 €.
- **Métrica principal:** coste por SQL. Secundarias: clic→formulario, MQL→SQL, % de MQL que son hoteles (hoy 19 de 122).
- **Test:** nueva landing vs. `chekin-hoteles` (Google) y vs. formulario instantáneo (Meta), 50/50, mínimo 4 semanas o 100 formularios por variante.
- **Evento de conversión:** envío del formulario HubSpot → Google Ads (conversión offline/importada desde HubSpot por SQL) y Meta (Conversions API con evento SQL).

## 10. Pendientes
- Testimonio real de hotel (nombre, cargo, hotel, cifra).
- Logos oficiales de PMS (Mews, Cloudbeds, Little Hotelier, eviivo, Amenitiz…) en File Manager.
- Fuente Proxima Nova (se usa Montserrat de momento).
- Tiempo de respuesta de ventas y tiempo de implantación para la FAQ.
- Términos de búsqueda de la PMax Competitors.
