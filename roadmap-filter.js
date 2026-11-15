// Open / Shipped / All switch for the roadmap table (session 71).
//
// build.py marks each row data-roadmap="open" or "done" and leaves an empty
// <div class="roadmap-filter"> before the table. Without this script every
// row shows. With it, open rows show by default; ?show=shipped or ?show=all
// picks another view and is kept in the address bar, so a view can be linked.
(function () {
  var slot = document.querySelector('.roadmap-filter');
  if (!slot) return;
  var rows = Array.prototype.slice.call(document.querySelectorAll('tr[data-roadmap]'));
  var views = [
    { key: 'open', label: 'Open', match: function (r) { return r.dataset.roadmap === 'open'; } },
    { key: 'shipped', label: 'Shipped', match: function (r) { return r.dataset.roadmap === 'done'; } },
    { key: 'all', label: 'All', match: function () { return true; } },
  ];
  var list = document.createElement('div');
  list.className = 'tablist';
  list.setAttribute('role', 'group');
  list.setAttribute('aria-label', 'Show roadmap items');
  var buttons = views.map(function (v) {
    var b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('role', 'tab');
    b.textContent = v.label + ' (' + rows.filter(v.match).length + ')';
    b.addEventListener('click', function () { show(v, true); });
    list.appendChild(b);
    return b;
  });
  slot.appendChild(list);

  function show(v, push) {
    rows.forEach(function (r) { r.hidden = !v.match(r); });
    views.forEach(function (w, i) { buttons[i].setAttribute('aria-selected', w === v ? 'true' : 'false'); });
    if (!push) return;
    var url = new URL(location.href);
    if (v.key === 'open') url.searchParams.delete('show'); else url.searchParams.set('show', v.key);
    history.replaceState(null, '', url);
  }
  var asked = new URLSearchParams(location.search).get('show');
  show(views.filter(function (v) { return v.key === asked; })[0] || views[0], false);
})();
