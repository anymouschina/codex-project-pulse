const { test } = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');

test('favicon and title follow known native unread state and clear on unavailable data', () => {
  const favicon = { href: '/assets/icon-outline.svg', dataset: { unreadIcon: '/assets/icon-unread.svg' } };
  const document = { querySelector: () => favicon, title: '' };
  const window = {};
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../src/project_pulse/web/brand.js'), 'utf8'), { document, window });
  const update = window.PulseBrand.update;
  update({ unreadBadge: { known: true, count: 2 } });
  assert.equal(favicon.href, '/assets/icon-unread.svg');
  assert.match(document.title, /^\(2\)/);
  update({ unreadBadge: { known: true, count: 1 } });
  assert.match(document.title, /^\(1\)/);
  update({ unreadBadge: { known: true, count: 0 } });
  assert.equal(favicon.href, '/assets/icon-outline.svg');
  assert.equal(document.title, 'Project Pulse · 项目总控台');
  update({ unreadBadge: { known: true, count: 3 } });
  update({ unreadBadge: { known: false, count: null } });
  assert.equal(favicon.href, '/assets/icon-outline.svg');
  update({ unreadBadge: { known: true, count: 3 } });
  update({ unreadBadge: { known: true, count: 3 } }, true);
  assert.equal(favicon.href, '/assets/icon-outline.svg');
  assert.equal(document.title, 'Project Pulse · 项目总控台');
});
