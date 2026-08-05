document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".nav-toggle");
  const navigation = document.querySelector("#site-navigation");

  if (!toggle || !navigation) return;

  const setOpen = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
    navigation.classList.toggle("is-open", open);
  };

  toggle.addEventListener("click", () => {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest(".nav-link")) setOpen(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setOpen(false);
      toggle.focus();
    }
  });

  const desktop = window.matchMedia("(min-width: 769px)");
  const closeOnDesktop = (event) => {
    if (event.matches) setOpen(false);
  };

  if (desktop.addEventListener) {
    desktop.addEventListener("change", closeOnDesktop);
  } else {
    desktop.addListener(closeOnDesktop);
  }
});
