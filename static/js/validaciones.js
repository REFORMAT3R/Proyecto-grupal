document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const parejas = document.getElementById("parejas");
  const celular = document.getElementById("celular");

  form.addEventListener("submit", (e) => {
    if (parejas.value <= 0) {
      alert("La cantidad de parejas debe ser mayor a 0");
      e.preventDefault();
    }

    if (!/^\d{9}$/.test(celular.value)) {
      alert("El celular debe tener 9 dígitos");
      e.preventDefault();
    }
  });
});
