# Logo 与入口状态

## 品牌资产

基础标志是透明背景、单色的叠卡 P，不包含装饰蓝点。

| 文件 | 用途 |
| --- | --- |
| `assets/logo.png` | 品牌主图，AI 生成后移除装饰点 |
| `assets/icon-outline.svg` / `icon-outline-dark.svg` | 浅色 / 深色线性矢量，60×60 viewBox |
| `assets/icon-solid.svg` / `icon-solid-dark.svg` | 页面内选中态实心矢量 |
| `assets/icon-unread.svg` | 浏览器未读 favicon |
| `assets/entrypoint-outline.png` / `entrypoint-outline-dark.png` | MCP 基础入口图标，无圆点 |
| `assets/entrypoint-unread.png` / `entrypoint-unread-dark.png` | MCP 候选未读图标，含蓝色状态点 |

PNG 由对应线性 SVG 使用 `@resvg/resvg-js@2.6.2` 导出为 120×120。未读版追加圆点 `cx=51, cy=9, r=7, fill=#0086d8, stroke-width=3`；浅色 halo 为白色，深色为 `#212121`。渲染器只用于资产制作，不是插件运行依赖。

## 公开接口调研（2026-11-17）

| 字段 / 规范 | 已确认用途 |
| --- | --- |
| `interface.composerIcon` / `composerIconDark` | 输入框图标及深色主题版本 |
| `interface.logo` / `logoDark` | 插件列表主图标及深色主题版本 |
| MCP `Tool.icons` | 入口优先使用的图标；支持格式、大小及 `theme: light/dark` |
| `serverInfo.icons` | 本地服务器入口图标回退 |
| 选中 / 未选中资源 | 当前公开 schema 未找到对应字段；深色主题不等于选中态 |
| 独立原生未读角标 | 当前公开 schema 未找到对应字段；合成图标不等于原生角标 API |

官方建议使用透明底、单色线性导航图标。第三方插件没有已文档化的 selected / active 双态注册方式。本项目不增加猜测字段，也不修改宿主界面。

参考：

- [插件图标字段](https://developers.openai.com/plugins/deploy/submission#icons)
- [图标设计与缓存](https://github.com/openai/mcp-extensions/blob/main/docs/patterns.md#icons)
- [入口图标优先级](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#entrypoint-icons)
- [MCP Icon schema](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2026-07-28/schema.ts)
- [工具列表变更通知](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#list-changed-notification)

## 状态与更新

`unreadBadge` 只统计已导入项目、未归档主会话中经桌面索引确认的未读。仍在运行的会话可以保留旧结果的未读；完成未读收件箱另有完成条件。全部已读、状态未知或数据不可用时不显示蓝点。

页面导航与 favicon 每次快照后更新。打开面板、切换导航不改写阅读状态。MCP 初始化和 `tools/list` 都返回当前未读对应的 PNG 图标；初始化后每 8 秒检查一次，仅在有 / 无未读发生变化时发送 `notifications/tools/list_changed`。宿主是否重新读取和绘制入口取决于客户端，且官方文档说明入口与图标会被缓存。

## 0.1.11 修复与验收边界

用户提供的原生全屏插件截图已经显示新版顶部导航，系统入口也有选中背景，但 P 仍为线性，图标上的点呈灰色。此现象不能归因于打开了 localhost 网页，也不能根据页面内蓝点宣称原生成功。

本版修复首次连接的服务器回退图标没有使用当前未读状态的问题，并把入口图标改为 PNG，尝试避免 SVG 专属模板着色。宿主仍可能统一着色；PNG 不是受支持的独立角标方案。

- 协议可验证：未读状态选择、浅深色资产、首连与工具图标一致、工具列表变更通知、版本化 HTML。
- 页面内已实现：选中实心、未选中线性、独立未读蓝点。
- 原生待验证：PNG 蓝点颜色和未读变化后的实时刷新。
- 原生未实现：选中 / 未选中的线性与实心切换；尚未找到公开接口。

当前 Computer Use 工具禁止访问 Codex 原生应用，不能直接完成系统入口视觉验收。未绕过限制，也未用 Chrome 预览替代原生结果。
