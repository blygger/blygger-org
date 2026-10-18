// Tabs for markdown pages (session 38, the contributors page).
//
// A page opts in with consecutive <section class="tab-panel" data-tab="slug"
// data-label="Label" markdown="1"> blocks inside <div class="tabset">. Without
// this script, or without JS, every panel shows, stacked under its own
// headings — the page never depends on it. With it, one panel shows at a time,
// and the hash picks the panel: #slug, or any anchor inside a panel (so the
// "On this page" rail and the Contents drawer still land, on whichever tab
// holds the heading).
(function () {
  document.querySelectorAll('.tabset').forEach(function (set) {
    var panels = Array.prototype.slice.call(set.querySelectorAll(':scope > .tab-panel'));
    if (panels.length < 2) return;
    var list = document.createElement('div');
    list.setAttribute('role', 'tablist');
    list.className = 'tablist';
    var tabs = panels.map(function (p, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('role', 'tab');
      b.id = 'tab-' + p.dataset.tab;
      b.setAttribute('aria-controls', p.id || (p.id = 'panel-' + p.dataset.tab));
      b.textContent = p.dataset.label || p.dataset.tab;
      p.setAttribute('role', 'tabpanel');
      p.setAttribute('aria-labelledby', b.id);
      b.addEventListener('click', function () {
        show(i, false);
        history.replaceState(null, '', '#' + p.dataset.tab);
      });
      b.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        show((i + d + panels.length) % panels.length, true);
      });
      list.appendChild(b);
      return b;
    });
    set.insertBefore(list, panels[0]);
    set.classList.add('tabbed');

    // Section lists outside the tabset (the "On this page" rail and the
    // Contents drawer) list every heading on the page. Show only the open
    // panel's, renumbered from 01, so the list matches what is on screen.
    var railItems = Array.prototype.slice.call(document.querySelectorAll('li'))
      .map(function (li) {
        var a = li.querySelector('a[href^="#"]');
        var target = a && document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
        var owner = target && panels.filter(function (p) { return p.contains(target); })[0];
        return owner && !set.contains(li) ? { li: li, owner: owner, idx: li.querySelector('.idx') } : null;
      })
      .filter(Boolean);
    function syncRail(open) {
      var counts = new Map();
      railItems.forEach(function (r) {
        var off = r.owner !== open;
        r.li.hidden = off;
        r.li.style.display = off ? 'none' : ''; // the rail's CSS sets display on li
        if (off || !r.idx) return;
        var k = (counts.get(r.li.parentNode) || 0) + 1;
        counts.set(r.li.parentNode, k);
        r.idx.textContent = (k < 10 ? '0' : '') + k;
      });
    }

    function show(n, focus) {
      panels.forEach(function (p, i) {
        p.hidden = i !== n;
        tabs[i].setAttribute('aria-selected', i === n ? 'true' : 'false');
        tabs[i].tabIndex = i === n ? 0 : -1;
      });
      if (railItems.length) syncRail(panels[n]);
      if (focus) tabs[n].focus();
    }
    function fromHash() {
      var h = decodeURIComponent(location.hash.slice(1));
      if (!h) return 0;
      for (var i = 0; i < panels.length; i++) {
        if (panels[i].dataset.tab === h) return i;
        var t = document.getElementById(h);
        if (t && panels[i].contains(t)) return i;
      }
      return -1;
    }
    var start = fromHash();
    show(start < 0 ? 0 : start, false);
    window.addEventListener('hashchange', function () {
      var n = fromHash();
      if (n < 0) return;
      show(n, false);
      var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (t && !panels.some(function (p) { return p.dataset.tab === t.id; })) t.scrollIntoView();
    });
  });
})();
