# Reporte de Errores

## Anexo 2: Informe de Errores Encontrados

Durante la fase de pruebas del **Sistema de Reservas de Canchas FISI**, se detectaron y corrigieron los siguientes errores:

---

| ID Defecto | Descripción del Defecto | Pasos para Reproducir | Fecha del Defecto | Detectado por (Tester) | Estado del Defecto | Corregido por | Fecha de Cierre | Prioridad |
|-----------|------------------------|----------------------|------------------|----------------------|-------------------|--------------|----------------|----------|
| **DEF-01** | El selector de horarios no se deshabilitaba cuando todas las franjas estaban bloqueadas | 1. Acceder a `reservas.html` <br> 2. Seleccionar una fecha bloqueada completamente <br> 3. Observar que el selector de horarios permanece habilitado | 2025-11-20 | Luis Gutierrez | ✅ CERRADO | Piero Badillo | 2025-11-21 | **Media** |
| **DEF-02** | El sistema permitía crear reservas en fechas pasadas desde la UI (validación solo en backend) | 1. Modificar manualmente el HTML del `<input type="date">` <br> 2. Seleccionar una fecha pasada <br> 3. Intentar reservar <br> 4. El backend rechaza correctamente, pero la UI no muestra feedback claro | 2025-11-22 | Luis Gutierrez | ✅ CERRADO | Johan Reyes | 2025-11-22 | **Baja** |
| **DEF-03** | La función `hay_solapamiento()` no consideraba correctamente franjas consecutivas | 1. Reservar franja 10:00–12:00 <br> 2. Intentar reservar franja 12:00–14:00 (consecutiva, sin solapar) <br> 3. El sistema rechazaba la reserva incorrectamente | 2025-11-23 | Piero Badillo | ✅ CERRADO | Piero Badillo | 2025-11-23 | **Alta** |
| **DEF-04** | El panel de administración no mostraba el tipo de bloqueo en la lista de bloqueos | 1. Acceder a `admin_dashboard.html` <br> 2. Bloquear un día completo y una franja <br> 3. Ver lista de bloqueos <br> 4. No se distinguía si era bloqueo de día o de franja | 2025-11-24 | Luis Gutierrez | ✅ CERRADO | Johan Reyes | 2025-11-24 | **Baja** |
| **DEF-05** | Al cancelar una reserva, el frontend no recargaba automáticamente la lista de reservas | 1. Acceder a `mis_reservas.html` <br> 2. Cancelar una reserva <br> 3. La reserva seguía apareciendo en la lista hasta recargar manualmente la página | 2025-11-25 | Luis Gutierrez | ✅ CERRADO | Johan Reyes | 2025-11-25 | **Media** |

---

## Detalle de Errores Corregidos

### DEF-01: Selector de horarios no se deshabilitaba

**Descripción:**  
Cuando se consultaba la disponibilidad de una fecha bloqueada completamente, el selector de horarios (`<select id="horarios">`) permanecía habilitado, pero mostraba el mensaje "⚠️ Reservas bloqueadas para esta fecha".

**Pasos:**
1. Ingresar a `reservas.html`.
2. Seleccionar fecha: `2025-12-01` (bloqueada).
3. Observar que el selector sigue habilitado.

**Solución implementada:**
```javascript
if (bloqueados === total && total > 0) {
    const opt = document.createElement("option");
    opt.textContent = "⚠️ Reservas bloqueadas para esta fecha";
    horarios.appendChild(opt);
    horarios.disabled = true; // ✅ Línea añadida
    return;
}
```

**Corregido por:** Piero Badillo  
**Fecha de cierre:** 2025-11-21

---

### DEF-03: Función de solapamiento rechazaba franjas consecutivas

**Descripción:**  
La función `hay_solapamiento()` implementaba la condición `h_ini1 < h_fin2 and h_ini2 < h_fin1`, que incorrectamente rechazaba franjas consecutivas como 10:00–12:00 y 12:00–14:00.

**Pasos:**
1. Reservar franja 10:00–12:00 para el usuario 1.
2. Intentar reservar franja 12:00–14:00 para el mismo usuario.
3. El sistema rechazaba con error "Esa franja choca con una reserva existente".

**Evidencia:**
```
Request: POST /reservas/crear
{
  "usuario_id": 1,
  "fecha": "2025-11-28",
  "hora_inicio": "12:00"
}

Response: HTTP 400
{
  "detail": "Esa franja choca con una reserva existente."
}
```

**Solución implementada:**
```python
# Antes (incorrecto):
if h_ini_nueva < h_fin_exist and h_ini_exist < h_fin_nueva:
    raise HTTPException(400, "Esa franja choca con una reserva existente.")

# Después (correcto):
if h_ini_nueva < h_fin_exist and h_ini_exist < h_fin_nueva and h_ini_nueva != h_fin_exist:
    raise HTTPException(400, "Esa franja choca con una reserva existente.")
```

**Corregido por:** Piero Badillo  
**Fecha de cierre:** 2025-11-23  
**Prioridad:** Alta

---

### DEF-05: Lista de reservas no se recargaba automáticamente

**Descripción:**  
Al cancelar una reserva desde `mis_reservas.html`, la reserva cancelada seguía apareciendo en la lista hasta que el usuario recargaba manualmente la página.

**Pasos:**
1. Acceder a `mis_reservas.html`.
2. Cancelar una reserva.
3. Observar que la reserva sigue visible en la lista.

**Solución implementada:**
```javascript
async function cancelar(id) {
    if (!confirm("¿Cancelar reserva?")) return;

    await apiCancelarReserva(id);
    alert("Reserva cancelada.");
    location.reload(); // ✅ Línea añadida para recargar automáticamente
}
```

**Corregido por:** Johan Reyes  
**Fecha de cierre:** 2025-11-22

---

## Resumen de Errores

- **Total de defectos detectados:** 5
- **Defectos corregidos:** 5
- **Defectos pendientes:** 0
- **Prioridad alta:** 1
- **Prioridad media:** 2
- **Prioridad baja:** 2

---

## Conclusión

Todos los errores detectados durante la fase de pruebas han sido corregidos exitosamente. El sistema cumple con los requisitos funcionales definidos y opera correctamente en todos los casos de uso probados.
