// Validar rol
const user = JSON.parse(localStorage.getItem("user"));
if (!user || user.rol !== "admin") {
    alert("Acceso denegado");
    window.location.href = "login.html";
}

// Cerrar sesión
document.getElementById("logoutBtn").addEventListener("click", () => {
    localStorage.clear();
    window.location.href = "login.html";
});

// ----------------------
// MANEJO DE BLOQUEOS
// ----------------------

document.getElementById("btnVerBloqueos").addEventListener("click", async () => {
    const fecha = document.getElementById("fecha").value;
    if (!fecha) return alert("Seleccione una fecha");

    try {
        const data = await apiObtenerBloqueos(fecha);
        renderBloqueos(data);
    } catch (e) {
        console.error(e);
        alert("Error al obtener bloqueos");
    }
});

function renderBloqueos(data) {
    const container = document.getElementById("bloqueosLista");
    if (data.length === 0) {
        container.innerHTML = "<p class='text-gray'>No hay bloqueos para esta fecha.</p>";
        return;
    }

    let html = "<ul style='list-style: none; padding: 0;'>";
    data.forEach(b => {
        html += `
            <li style="background: var(--background-color); padding: 0.5rem; margin-bottom: 0.5rem; border-radius: var(--radius-md); display: flex; justify-content: space-between; align-items: center;">
                <span>
                    <strong>${b.tipo === 'dia_completo' ? 'Día Completo' : 'Franja'}</strong>
                    ${b.hora_inicio ? `(${b.hora_inicio} - ${b.hora_fin})` : ''}
                </span>
                <button onclick="desbloquear(${b.id})" style="color: var(--error-color); background: none; border: none; cursor: pointer; font-weight: 600;">Eliminar</button>
            </li>
        `;
    });
    html += "</ul>";
    container.innerHTML = html;
}

// Bloquear día
document.getElementById("btnBloquearDia").addEventListener("click", async () => {
    const fecha = document.getElementById("fecha").value;
    if (!fecha) return alert("Seleccione una fecha");

    if (!confirm("¿Seguro que desea bloquear todo el día?")) return;

    try {
        const r = await apiBloquearDia(fecha);
        alert(r.msg);
        // Recargar bloqueos
        document.getElementById("btnVerBloqueos").click();
    } catch (e) {
        alert("Error al bloquear día");
    }
});

// Bloquear franja
document.getElementById("btnBloquearFranja").addEventListener("click", async () => {
    const fecha = document.getElementById("fecha").value;
    const hora = document.getElementById("franja").value;
    if (!fecha) return alert("Seleccione una fecha");

    try {
        const r = await apiBloquearFranja(fecha, hora);
        alert(r.msg);
        // Recargar bloqueos
        document.getElementById("btnVerBloqueos").click();
    } catch (e) {
        alert("Error al bloquear franja");
    }
});

// Desbloquear
async function desbloquear(id) {
    if (!confirm("¿Eliminar bloqueo?")) return;
    try {
        const r = await apiDesbloquear(id);
        alert(r.msg);
        document.getElementById("btnVerBloqueos").click();
    } catch (e) {
        alert("Error al desbloquear");
    }
}

// ----------------------
// CONSULTAR DISPONIBILIDAD
// ----------------------

document.getElementById("btnConsultarDisp").addEventListener("click", async () => {
    const fecha = document.getElementById("fecha_disp").value;
    if (!fecha) return alert("Seleccione una fecha");

    try {
        const data = await apiDisponibilidad(fecha);
        renderDisponibilidad(data);
    } catch (e) {
        console.error(e);
        alert("Error al consultar disponibilidad");
    }
});

function renderDisponibilidad(data) {
    const container = document.getElementById("resultadoDisp");

    if (!data || data.length === 0) {
        container.innerHTML = "<p>No hay información disponible.</p>";
        return;
    }

    let html = `
        <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
            <thead>
                <tr style="text-align: left; border-bottom: 2px solid var(--border-color);">
                    <th style="padding: 0.5rem;">Horario</th>
                    <th style="padding: 0.5rem;">Estado</th>
                </tr>
            </thead>
            <tbody>
    `;

    data.forEach(slot => {
        let color = "var(--text-primary)";
        let estado = "Disponible";

        if (slot.estado === "reservado") {
            color = "var(--error-color)";
            estado = "Reservado";
        } else if (slot.estado === "bloqueado") {
            color = "var(--text-secondary)";
            estado = "Bloqueado";
        } else {
            color = "var(--secondary-color)";
        }

        html += `
            <tr style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 0.5rem;">${slot.inicio} - ${slot.fin}</td>
                <td style="padding: 0.5rem; color: ${color}; font-weight: 600;">${estado}</td>
            </tr>
        `;
    });

    html += "</tbody></table>";
    container.innerHTML = html;
}
