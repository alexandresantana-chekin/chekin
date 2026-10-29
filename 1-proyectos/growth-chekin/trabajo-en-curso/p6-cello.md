# P6 · Cello (programa de referidos)

Con Valery Saavedra. Plan para el 6/11. Tarea en Asana Growth Daily › Alexandre y ficha P6 en Notion.

## Reunión con Cello · 29/10/2026
Resumen enviado por Cello a Valery por Slack (Connect con Cello) tras la reunión.

**Datos que da Cello** (H-45):
- Desde el lanzamiento en junio: **10 clientes referidos** han pagado. Octubre, el mejor mes hasta ahora.
- Usuarios con Cello activado: **~12.000**, frente a los **~150.000** que esperaba Chekin.

**Pendiente de Cello:**
- Errores UCC en el portal: lo revisan con su soporte (¿solo un fallo de visualización del portal nuevo?).
- Documentación de integración para el equipo técnico: eventos, cruce de `new_user_id` y comprobaciones de fraude, para arreglar de raíz las recompensas atascadas en «pending». https://docs.cello.so/integrations/webhooks/stripe-webhook
- Opcional: lista de 20–25 partners posibles con su herramienta de búsqueda de partners. Hay que pedírsela.

**Pendiente de Chekin:**
1. **Usuarios activados (~12k vs ~150k):** preguntar a Tecnología si hay un filtro por segmento o un despliegue parcial.
2. **Arrancar Cello al iniciar sesión** en los clientes nuevos: así las comprobaciones de fraude se resuelven solas y las recompensas no se quedan en «pending». Confirmar que el `new_user_id` enviado a Stripe coincide con el `productUserId` con el que se arranca Cello. https://docs.cello.so/guides/integration/pre-launch-testbook#referral-component
3. **Dar de alta a los 5 partners** cuando la configuración esté confirmada: invitarlos desde Partner Users y dejar vacío el Product User ID si no son usuarios de Chekin. https://docs.cello.so/guides/partners/manage-partners

**Siguiente palanca, cuando lo básico funcione:** pedir el referido en momentos de satisfacción, por ejemplo cuando el usuario conecta su primera propiedad. https://docs.cello.so/guides/best-practices/contextual-sharing

**Para el plan del 6/11 [POR COMPROBAR]:** quién es el contacto técnico de Chekin para los puntos 1 y 2; MRR de los 10 referidos (Leopard); a qué KPI se ata el programa (referidos/mes, conversión del referido, MRR referido).
