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

    function show(n, focus) {
      panels.forEach(function (p, i) {
        p.hidden = i !== n;
        tabs[i].setAttribute('aria-selected', i === n ? 'true' : 'false');
        tabs[i].tabIndex = i === n ? 0 : -1;
      });
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
