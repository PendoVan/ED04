const API = "http://127.0.0.1:8000";

async function login() {
    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ correo, password })
    });

    const data = await res.json();

    if (!res.ok) {
        return alert(data.detail || "Error desconocido");
    }

    // Guardar sesión
    localStorage.setItem("user", JSON.stringify(data));

    // VERIFICAR ROL
    console.log("ROL DETECTADO:", data.rol);

    if (data.rol === "admin") {
        window.location.href = "panel_admin.html";
    } else {
        window.location.href = "reservar.html"; 
    }
}

async function apiLogin(correo, password) {
    const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ correo, password })
    });

    if (!response.ok) {
        throw new Error("Credenciales incorrectas");
    }

    return await response.json();
}


document.getElementById("formLogin").addEventListener("submit", async (e) => {
    e.preventDefault();

    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;

    try {
        const data = await apiLogin(correo, password);

        // Guardamos los datos en localStorage
        localStorage.setItem("usuario_id", data.id);
        localStorage.setItem("usuario_correo", data.correo);
        localStorage.setItem("usuario_rol", data.rol);

        // 🔥 REDIRECCIÓN SEGÚN ROL 🔥
        if (data.rol === "admin") {
            window.location.href = "admin_dashboard.html";  // ⬅️ TU PANEL DEL ADMIN
        } else {
            window.location.href = "reservas.html";         // ⬅️ Página del estudiante
        }

    } catch (error) {
        alert("Error al iniciar sesión. Verifique sus credenciales.");
        console.error(error);
    }
});

