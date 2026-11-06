// MARTIUS TATTOO STUDIO — script principale
document.addEventListener("DOMContentLoaded", () => {
  // Menu mobile
  const burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", () => {
      const open = document.body.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", open);
    });
    document.querySelectorAll(".main-nav a").forEach(a =>
      a.addEventListener("click", () => document.body.classList.remove("nav-open"))
    );
  }

  // Animazioni allo scroll
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll(".reveal").forEach(el => io.observe(el));

  // Filtri galleria
  document.querySelectorAll(".filters").forEach(group => {
    const gallery = document.querySelector(group.dataset.target);
    group.addEventListener("click", e => {
      const btn = e.target.closest("button");
      if (!btn) return;
      group.querySelectorAll("button").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const f = btn.dataset.filter;
      gallery.querySelectorAll("figure").forEach(fig => {
        fig.classList.toggle("hide", f !== "all" && !fig.dataset.cat.split(" ").includes(f));
      });
    });
  });

  // Lightbox
  const lb = document.createElement("div");
  lb.className = "lightbox";
  lb.innerHTML = '<img alt="">';
  document.body.appendChild(lb);
  document.querySelectorAll(".gallery figure").forEach(fig => {
    fig.addEventListener("click", () => {
      lb.querySelector("img").src = fig.dataset.full;
      lb.querySelector("img").alt = fig.getAttribute("aria-label") || "";
      lb.classList.add("open");
    });
  });
  lb.addEventListener("click", () => lb.classList.remove("open"));
  document.addEventListener("keydown", e => { if (e.key === "Escape") lb.classList.remove("open"); });

  // Carosello artisti
  const track = document.querySelector(".artists-track");
  document.querySelectorAll("[data-scroll]").forEach(b =>
    b.addEventListener("click", () => track.scrollBy({ left: 302 * Number(b.dataset.scroll), behavior: "smooth" }))
  );

  // Modulo prenotazione -> apre l'email già compilata
  const form = document.querySelector("#booking-form");
  if (form) {
    form.addEventListener("submit", e => {
      e.preventDefault();
      const d = Object.fromEntries(new FormData(form));
      const body =
        `Nome: ${d.nome}\nTelefono: ${d.telefono}\nEmail: ${d.email}\n` +
        `Servizio: ${d.servizio}\nArtista: ${d.artista}\nZona del corpo: ${d.zona}\n\n${d.messaggio}`;
      window.location.href =
        `mailto:${form.dataset.email}?subject=${encodeURIComponent("Richiesta appuntamento - " + d.servizio)}&body=${encodeURIComponent(body)}`;
    });
  }

  // Anno nel footer
  document.querySelectorAll(".year").forEach(el => (el.textContent = new Date().getFullYear()));
});
