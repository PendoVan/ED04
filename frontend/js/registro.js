document.getElementById("formRegistro").addEventListener("submit", async (e) => {
    e.preventDefault();

    const correo = document.getElementById("correo").value;
    const password = document.getElementById("password").value;

    const respuesta = await apiRegistro(correo, password);

    if (respuesta.detail) {
        document.getElementById("mensaje").innerText = "❌ " + respuesta.detail;
    } else {
        document.getElementById("mensaje").innerText = "✔ Usuario registrado correctamente";
    }
});
