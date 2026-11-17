# Bundled browser dependencies

The browser page loads these files locally. `ui_resource.py` embeds the same
files into the MCP App resource, so neither host needs a runtime CDN connection.

| Package | Version | Files in use | License |
| --- | --- | --- | --- |
| lucide | 0.468.0 | `lucide.min.js` | ISC; `LICENSE-lucide` |
| tom-select | 2.4.3 | `tom-select.complete.min.js`, `tom-select.css` | Apache-2.0; `LICENSE-tom-select` |
| flatpickr | 4.6.13 | `flatpickr.min.js`, `flatpickr.min.css`, `flatpickr-zh.js` | MIT; `LICENSE-flatpickr` |

Tom Select and Flatpickr are the upstream npm distribution files, obtained via
`npm pack tom-select@2.4.3` and `npm pack flatpickr@4.6.13`. The Chinese locale is
`flatpickr/dist/l10n/zh.js`, copied as `flatpickr-zh.js`. Application-specific
styling and behavior belong in `../components.css` and `../components.js`;
do not edit the vendored libraries.
