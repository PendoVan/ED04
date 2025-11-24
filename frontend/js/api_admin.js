const API_URL = "http://127.0.0.1:8000";

// Obtener bloqueos
async function apiObtenerBloqueos(fecha) {
    const r = await fetch(`${API_URL}/admin/bloqueos/${fecha}`);
    return await r.json();
}

// Bloquear día
async function apiBloquearDia(fecha) {
    const r = await fetch(`${API_URL}/admin/bloquear_dia?fecha=${fecha}`, {
        method: "POST"
    });
    return await r.json();
}

// Bloquear franja
async function apiBloquearFranja(fecha, hora) {
    const r = await fetch(`${API_URL}/admin/bloquear_franja?fecha=${fecha}&hora_inicio=${hora}`, {
        method: "POST"
    });
    return await r.json();
}

// Desbloquear
async function apiDesbloquear(id) {
    const r = await fetch(`${API_URL}/admin/desbloquear/${id}`, {
        method: "DELETE"
    });
    return await r.json();
}
