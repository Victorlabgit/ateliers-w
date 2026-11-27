// Ateliers W — formulaire de devis (Formspree), bannière newsletter, suivi Umami
document.querySelectorAll('form[action*="formspree"]').forEach(form => {
  const retour = form.querySelector('.retour');
  form.addEventListener('submit', async e => {
    e.preventDefault();
    retour.textContent = '';
    try {
      const r = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
      if (!r.ok) throw new Error();
      form.reset();
      retour.textContent = 'Merci, votre demande a bien été envoyée. Nous vous répondons rapidement.';
      if (window.umami) umami.track('devis-submit', { service: (form.querySelector('[name=service]') || {}).value || '' });
    } catch {
      retour.textContent = "L'envoi a échoué, réessayez plus tard ou écrivez-nous par e-mail.";
    }
  });
});

// Bannière de confirmation après inscription à la newsletter (?subscribed=1)
(function () {
  const p = new URLSearchParams(location.search);
  if (p.get('subscribed') === '1' || p.get('newsletter') === 'confirmee') {
    const b = document.querySelector('.bandeau-ok');
    if (b) { b.hidden = false; setTimeout(() => { b.hidden = true; }, 7000); }
    if (window.umami) umami.track('newsletter-confirmed');
  }
})();

// Inscription newsletter (Brevo) sans quitter la page
document.querySelectorAll('form.newsletter__form').forEach((form) => {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    let msg = form.querySelector('.newsletter__retour');
    if (!msg) { msg = document.createElement('p'); msg.className = 'newsletter__retour'; msg.setAttribute('role', 'status'); form.appendChild(msg); }
    const btn = form.querySelector('button[type=submit]');
    if (btn) btn.disabled = true;
    try {
      const r = await fetch(form.action, { method: 'POST', body: new FormData(form) });
      const d = await r.json();
      if (d.success) {
        form.reset();
        msg.textContent = d.message || 'Merci ! Confirmez votre inscription grâce au lien reçu par e-mail.';
      } else {
        msg.textContent = (d.errors && Object.values(d.errors)[0]) || "L'inscription n'a pas pu être enregistrée. Merci de réessayer.";
      }
    } catch {
      msg.textContent = "L'inscription n'a pas pu être enregistrée. Merci de réessayer.";
    }
    if (btn) btn.disabled = false;
  });
});
