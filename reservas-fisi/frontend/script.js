const API_URL = "http://127.0.0.1:8000/reservas";

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
