const API_URL = "https://zany-yodel-7vww4qg94x7xhwq5w-8000.app.github.dev";

document.getElementById("formReserva").addEventListener("submit", async (e) => {
  e.preventDefault();
  const usuario = document.getElementById("usuario").value;
  const cancha = document.getElementById("cancha").value;
  const fecha = document.getElementById("fecha").value;

  const params = new URLSearchParams({ usuario, cancha, fecha });
  const res = await fetch(`${API_URL}?${params.toString()}`, { method: "POST" });
  const data = await res.json();

  document.getElementById("output").textContent = data.mensaje;
});
