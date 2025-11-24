const user = JSON.parse(localStorage.getItem("user"));
if (!user) window.location.href = "login.html";

async function cargarDisponibilidad() {
    const fecha = document.getElementById("fecha").value;
    const horarios = document.getElementById("horarios");

    horarios.innerHTML = "";
    horarios.disabled = false;

    if (!fecha) return;

    const lista = await apiDisponibilidad(fecha);

    // Contadores
    let disponibles = 0;
    let bloqueados = 0;
    let reservados = 0;
    let total = lista.length;

    lista.forEach(f => {
        if (f.estado === "disponible") disponibles++;
        if (f.estado === "bloqueado") bloqueados++;
        if (f.estado === "reservado") reservados++;
    });

    // 1. Caso: Día completamente bloqueado (o todas las franjas bloqueadas)
    if (bloqueados === total && total > 0) {
        const opt = document.createElement("option");
        opt.textContent = "⚠️Reservas bloqueadas para esta fecha";
        horarios.appendChild(opt);
        horarios.disabled = true;
        return;
    }

    // 2. Caso: Todo reservado (sin bloqueos totales, pero lleno)
    if (disponibles === 0) {
        const opt = document.createElement("option");
        opt.textContent = "⚠️ Todas las franjas ya han sido reservadas.";
        horarios.appendChild(opt);
        horarios.disabled = true;
        return;
    }

    // 3. Caso normal: Mostrar disponibles
    lista.forEach(f => {
        if (f.estado === "disponible") {
            const opt = document.createElement("option");
            opt.value = `${f.inicio}|${f.fin}`;
            opt.textContent = `${f.inicio} - ${f.fin}`;
            horarios.appendChild(opt);
        }
    });

    // Si por alguna razón no entró en los casos anteriores pero no hay disponibles
    if (horarios.children.length === 0) {
        const opt = document.createElement("option");
        opt.textContent = "No hay horarios disponibles.";
        horarios.appendChild(opt);
        horarios.disabled = true;
    }
}

async function reservar() {
    const fecha = document.getElementById("fecha").value;
    const [hora_inicio, hora_fin] = document.getElementById("horarios").value.split("|");

    const data = {
        usuario_id: user.id,
        fecha,
        hora_inicio,
        hora_fin
    };

    const res = await apiCrearReserva(data);

    if (res.detail) {
        alert(res.detail);
        return;
    }

    alert("Reserva realizada.");
    window.location.href = "mis_reservas.html";
}
