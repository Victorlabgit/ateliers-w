// Envoi des formulaires via Formspree (remplacer VOTRE_ID dans le HTML)
document.querySelectorAll('form[action*="formspree"]').forEach(form => {
  const retour = form.querySelector('.retour');
  form.addEventListener('submit', async e => {
    e.preventDefault();
    retour.textContent = '';
    if (form.action.includes('VOTRE_ID')) {
      retour.textContent = 'Formulaire non configuré : remplacez VOTRE_ID par votre identifiant Formspree.';
      return;
    }
    try {
      const r = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
      if (!r.ok) throw new Error();
      form.reset();
      retour.textContent = 'Merci, votre message a bien été envoyé.';
    } catch {
      retour.textContent = "L'envoi a échoué, réessayez plus tard.";
    }
  });
});
