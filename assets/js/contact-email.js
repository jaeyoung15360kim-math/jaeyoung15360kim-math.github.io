document.addEventListener("DOMContentLoaded", () => {
  const target = document.querySelector("#contact-email");
  if (!target) return;

  const decode = (codes) => String.fromCharCode(...codes);
  const localPart = decode([106, 97, 101, 121, 111, 117, 110, 103, 107, 105, 109, 50, 50]);
  const domain = decode([115, 110, 117, 46, 97, 99, 46, 107, 114]);

  target.textContent = `${localPart} at ${domain}`;
});
