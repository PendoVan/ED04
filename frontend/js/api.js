const API = "http://127.0.0.1:8000";

// ===== AUTENTICACIÓN =====

async function apiLogin(data) {
    const res = await fetch(`${API}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    return res.json();
}

async function apiRegistro(data) {
    const res = await fetch(`${API}/auth/registro`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    return res.json();
}

// ===== RESERVAS =====

async function apiCrearReserva(data) {
    const res = await fetch(`${API}/reservas/crear`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    return res.json();
}

async function apiListarReservas(userId) {
    const res = await fetch(`${API}/reservas/${userId}`);
    return res.json();
}

async function apiCancelarReserva(id) {
    const res = await fetch(`${API}/reservas/${id}`, {
        method: "DELETE"
    });
    return res.json();
}

// ===== DISPONIBILIDAD =====

async function apiDisponibilidad(fecha) {
    const res = await fetch(`${API}/disponibilidad/${fecha}`);
    return res.json();
}
