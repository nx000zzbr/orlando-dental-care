// Orlando Dental Care · shared script for every page.
// 1. Language switch (English / Spanish), remembered across pages.
// 2. "Open now" badges from Orlando time.
// 3. The phone menu.
// 4. The contact form opens an email with the message filled in.

(() => {
  const root = document.documentElement;
  const button = document.getElementById('lang');
  const apply = (lang) => {
    root.dataset.lang = lang;
    root.lang = lang;
    try { localStorage.setItem('odc-lang', lang); } catch (e) { /* private window */ }
    document.querySelectorAll('option[data-en]').forEach((o) => { o.textContent = o.dataset[lang] || o.dataset.en; });
    updateOpenNow();
  };
  if (button) button.addEventListener('click', () => apply(root.dataset.lang === 'es' ? 'en' : 'es'));
  document.querySelectorAll('option[data-en]').forEach((o) => { o.textContent = o.dataset[root.dataset.lang] || o.dataset.en; });
  const q = new URLSearchParams(location.search).get('lang');
  if (q === 'es' || q === 'en') apply(q);
})();

// Hours: Monday to Friday, 9 to 5, Orlando time (America/New_York).
function updateOpenNow() {
  const els = document.querySelectorAll('[data-open-now]');
  if (!els.length) return;
  let parts;
  try {
    parts = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: false }).formatToParts(new Date());
  } catch (e) { return; }
  const get = (type) => (parts.find((p) => p.type === type) || {}).value;
  const day = get('weekday');
  const minutes = (Number(get('hour')) % 24) * 60 + Number(get('minute'));
  const weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].includes(day);
  const open = weekday && minutes >= 9 * 60 && minutes < 17 * 60;
  const es = document.documentElement.dataset.lang === 'es';
  let text;
  if (open) {
    text = (17 * 60 - minutes <= 60) ? (es ? 'Abierto, cierra pronto' : 'Open, closes soon') : (es ? 'Abierto ahora' : 'Open now');
  } else if (weekday && minutes < 9 * 60) {
    text = es ? 'Cerrado, abre a las 9' : 'Closed, opens at 9 a.m.';
  } else if (day === 'Fri' || day === 'Sat' || day === 'Sun') {
    text = es ? 'Cerrado, abre el lunes a las 9' : 'Closed, opens Monday at 9 a.m.';
  } else {
    text = es ? 'Cerrado, abre mañana a las 9' : 'Closed, opens tomorrow at 9 a.m.';
  }
  els.forEach((el) => { el.textContent = text; el.classList.toggle('is-closed', !open); });
}
updateOpenNow();
setInterval(updateOpenNow, 60000);

// Phone menu
(() => {
  const burger = document.getElementById('burger');
  const menu = document.getElementById('menu');
  if (!burger || !menu) return;
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
})();

// Contact form: build a mailto with the fields filled in (no backend yet).
(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const v = (id) => (document.getElementById(id) || {}).value || '';
    const reasonEl = document.getElementById('f-reason');
    const reason = reasonEl ? reasonEl.options[reasonEl.selectedIndex].textContent.trim() : '';
    const subject = `Website message: ${reason}`;
    const body = `Name: ${v('f-name')}\nContact: ${v('f-contact')}\nReason: ${reason}\n\n${v('f-msg')}`;
    location.href = `mailto:orlandodentalcare@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
})();

// Entrances: cards and section titles rise once as they come into view.
(() => {
  document.documentElement.classList.add('js');
  const targets = document.querySelectorAll('.card, .facts-row li, .section-title, .step, .timeline li, .faq, .postcards, .service-art');
  if (!targets.length || !('IntersectionObserver' in window)) return;
  targets.forEach((el, i) => { el.setAttribute('data-reveal', ''); });
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  targets.forEach((el) => io.observe(el));
  setTimeout(() => targets.forEach((el) => el.classList.add('is-in')), 3000);
})();
