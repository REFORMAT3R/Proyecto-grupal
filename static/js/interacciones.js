document.addEventListener("DOMContentLoaded", () => {
  const danza = document.getElementById("danza");
  const parejas = document.getElementById("parejas");

  const info = document.createElement("p");
  info.style.fontSize = "20px";
  danza.after(info);

  danza.addEventListener("change", () => {
    const textos = {
      "Wititi": "Traje tradicional del Colca.",
      "Caporales": "Traje elegante y vistoso.",
      "Tinkus": "Traje fuerte y colorido.",
      "Carnaval de Arequipa": "Traje festivo tradicional."
    };
    info.textContent = textos[danza.value] || "";
  });

  parejas.addEventListener("input", () => {
    info.textContent += ` | Parejas: ${parejas.value}`;
  });
});
