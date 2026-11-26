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
  if (p.get('subscribed') === '1') {
    const b = document.querySelector('.bandeau-ok');
    if (b) { b.hidden = false; setTimeout(() => { b.hidden = true; }, 7000); }
    if (window.umami) umami.track('newsletter-confirmed');
  }
})();
