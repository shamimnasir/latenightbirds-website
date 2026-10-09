const root = document.documentElement;
const $ = (id) => document.getElementById(id);

// theme toggle
$('themeToggle').addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  root.dataset.theme = next;
  try { localStorage.setItem('theme', next); } catch (e) {}
});

// mobile menu
const menuBtn = $('menuBtn'), nav = $('nav');
menuBtn.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
});
nav.addEventListener('click', (e) => { if (e.target.closest('a')) nav.classList.remove('open'); });

// header border on scroll
const hdr = $('hdr');
const onScroll = () => hdr.classList.toggle('scrolled', scrollY > 8);
addEventListener('scroll', onScroll, { passive: true }); onScroll();

// 24-hour "night shift" grid (home only)
const hours = $('hours');
if (hours) {
  for (let r = 0; r < 3; r++) {
    for (let h = 0; h < 24; h++) {
      const i = document.createElement('i');
      if (h >= 9 && h < 17) i.className = 'l1';
      else { i.className = 'l2'; if ((h + r) % 3 === 0) i.classList.add('pulse'); }
      hours.appendChild(i);
    }
  }
}

// scroll reveal
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// stat count-up
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('[data-count]').forEach((el) => {
  if (reduce) return;
  const target = +el.dataset.count, suffix = el.dataset.suffix || '';
  const t0 = performance.now(), dur = 1400;
  const tick = (t) => {
    const p = Math.min((t - t0) / dur, 1);
    el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
});

// active section in nav (home only)
const links = [...document.querySelectorAll('.nav a[href^="/#"]')];
if (location.pathname === '/' && links.length) {
  const secs = links.map((a) => document.getElementById(a.getAttribute('href').slice(2))).filter(Boolean);
  addEventListener('scroll', () => {
    let cur = null;
    secs.forEach((s) => { if (s.getBoundingClientRect().top < innerHeight * 0.4) cur = s; });
    links.forEach((a) => a.classList.toggle('active', !!cur && a.getAttribute('href') === '/#' + cur.id));
  }, { passive: true });
}
