# Changelog

## 0.1.11 — 2026-11-17

First public release, based on the local Project Pulse plugin.

- Added a GitHub-installable `project-pulse` marketplace and MIT license.
- Preserved the compact project dashboard, native-read-state inbox, linked todos and direct chat navigation.
- Fixed initial MCP server fallback icons to reflect current unread state.
- Exported light/dark entrypoint icons as 120×120 PNGs to try to avoid SVG template tinting. Native sidebar color and live refresh remain unverified; selected/outline-to-solid native switching is not implemented because no supported field has been found.
- Kept native UI resource addresses versioned to prevent cross-release HTML reuse.
- Added public installation guidance, anonymized QA notes and a CI workflow template.

Earlier versions were local development releases. Their private development history is not part of this public repository.
