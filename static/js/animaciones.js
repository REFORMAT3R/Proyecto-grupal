document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll("section");

  const mostrar = () => {
    sections.forEach(sec => {
      const pos = sec.getBoundingClientRect().top;
      if (pos < window.innerHeight - 100) {
        sec.classList.add("visible");
      }
    });
  };

  window.addEventListener("scroll", mostrar);
  mostrar();
});