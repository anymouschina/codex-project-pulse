const { test } = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');

test('native MCP bridge initializes before tools and passes mutations without localhost requests', async () => {
  const listeners = {};
  const messages = [];
  let ctx;
  const host = {
    postMessage(message) {
      messages.push(message);
      if (message.id) queueMicrotask(() => listeners.message({source:host, data:{jsonrpc:'2.0', id:message.id, result:message.method==='ui/initialize'?{protocolVersion:'2026-01-26'}:{structuredContent:message.params.name==='dashboard_snapshot'?{projects:[],sessions:[],todos:[]}:{ok:true}}}}));
    }
  };
  const win = {addEventListener:(name,fn)=>{listeners[name]=fn;}};
  ctx = vm.createContext({window:win,parent:host,setTimeout,clearTimeout,Map,Error,Promise,JSON,decodeURIComponent,Date});
  vm.runInContext(fs.readFileSync(path.join(__dirname,'../src/project_pulse/web/mcp-bridge.js'),'utf8'),ctx);
  const initial = await win.PulseHost.request('/api/bootstrap');
  assert.equal(initial.token,'mcp-host');
  assert.equal(initial.data.projects.length,0);
  assert.equal(messages[0].method,'ui/initialize');
  assert.equal(messages[0].params.appInfo.version, JSON.parse(fs.readFileSync(path.join(__dirname, '../plugin.json'), 'utf8')).version);
  assert.equal(messages[1].method,'ui/notifications/initialized');
  const result = await win.PulseHost.request('/api/todo',{title:'Follow up',projectId:'p1'});
  assert.equal(result.ok,true);
  assert.equal(messages.at(-1).method,'tools/call');
  assert.equal(messages.at(-1).params.name,'dashboard_action');
  assert.equal(messages.at(-1).params.arguments.action,'todo');
  assert.equal(messages.at(-1).params.arguments.values.title,'Follow up');
});
