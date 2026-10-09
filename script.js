// theme toggle
const root = document.documentElement;
document.getElementById('themeToggle').addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  root.dataset.theme = next;
  try { localStorage.setItem('theme', next); } catch (e) {}
});

document.getElementById('year').textContent = new Date().getFullYear();

// 24-hour "night shift" grid: team works 9-17, automation covers the rest
const hours = document.getElementById('hours');
for (let r = 0; r < 3; r++) {
  for (let h = 0; h < 24; h++) {
    const i = document.createElement('i');
    const day = h >= 9 && h < 17;
    if (day) i.className = 'l1';
    else { i.className = 'l2'; if ((h + r) % 3 === 0) i.classList.add('pulse'); }
    hours.appendChild(i);
  }
}

// scroll reveal + count-up
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

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

// active nav link
const links = [...document.querySelectorAll('.nav a[href^="#"]')];
const secs = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
addEventListener('scroll', () => {
  let cur = secs[0];
  secs.forEach((s) => { if (s.getBoundingClientRect().top < innerHeight * 0.4) cur = s; });
  links.forEach((a) => a.classList.toggle('active', a.getAttribute('href') === '#' + cur.id));
}, { passive: true });
