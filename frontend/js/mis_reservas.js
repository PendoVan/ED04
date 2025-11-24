const user = JSON.parse(localStorage.getItem("user"));
if (!user) window.location.href = "login.html";

async function cargarReservas() {
    const lista = document.getElementById("lista");
    const res = await apiListarReservas(user.id);

    if (res.length === 0) {
        lista.innerHTML = "<p class='text-gray'>No tienes reservas activas.</p>";
        return;
    }

    res.forEach(r => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <div style="margin-bottom: 1rem;">
                <p class="text-sm text-gray">Fecha</p>
                <p style="font-weight: 600; font-size: 1.1rem;">${r.fecha}</p>
            </div>
            <div style="margin-bottom: 1.5rem;">
                <p class="text-sm text-gray">Horario</p>
                <p style="font-weight: 500;">${r.hora_inicio} — ${r.hora_fin}</p>
            </div>
            <button onclick="cancelar(${r.id})" class="btn btn-full" style="background-color: var(--error-color); color: white;">Cancelar Reserva</button>
        `;
        lista.appendChild(card);
    });
}

async function cancelar(id) {
    if (!confirm("¿Cancelar reserva?")) return;

    await apiCancelarReserva(id);
    alert("Reserva cancelada.");
    location.reload();
}

cargarReservas();
