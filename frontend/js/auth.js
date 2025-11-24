async function login() {
    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;

    const res = await apiLogin({ correo, password });

    if (res.detail) {
        alert(res.detail);
        return;
    }

    // Guardamos la sesión
    localStorage.setItem("user", JSON.stringify(res));

    // Redirección según rol
    if (res.rol === "admin") {
        window.location.href = "admin_dashboard.html";
    } else {
        window.location.href = "reservas.html";
    }
}

async function registro() {
    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;

    const res = await apiRegistro({ correo, password });

    if (res.detail) {
        alert(res.detail);
        return;
    }

    alert("Registro exitoso. Ahora inicia sesión.");
    window.location.href = "login.html";
}
