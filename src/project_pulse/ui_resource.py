"""Self-contained MCP App resource; no localhost fetch or external CDN required."""
from pathlib import Path
import re
import base64

from . import __version__
from .branding import ASSETS

ROOT = Path(__file__).resolve().parent / 'web'
# Hosts cache entrypoint HTML separately from the installed plugin. A new
# release must advertise a new resource identity to avoid reusing an old UI.
URI = f'ui://project-pulse/dashboard-{__version__}.html'
MIME = 'text/html;profile=mcp-app'


def resource():
    html = (ROOT / 'index.html').read_text()
    css = '\n'.join((ROOT / name).read_text() for name in ['vendor/tom-select.css', 'vendor/flatpickr.min.css', 'tokens.css', 'style.css', 'components.css'])
    css = re.sub(r'@import\s+url\([^)]*\);', '', css)
    html = re.sub(r'<link rel="stylesheet" href="[^"]+"\s*/>', '', html)
    html = html.replace('</head>', f'<meta name="project-pulse-version" content="{__version__}">' + '<style>' + css + '</style></head>')
    # The normal browser page stays unchanged. Only the resource uses host RPC.
    html = re.sub(r'<script src="([^"]+)" defer></script>', '', html)
    scripts = []
    for name in ['vendor/lucide.min.js', 'vendor/tom-select.complete.min.js', 'vendor/flatpickr.min.js', 'vendor/flatpickr-zh.js', 'components.js', 'brand.js', 'mcp-bridge.js', 'app.js']:
        scripts.append('<script>' + (ROOT / name).read_text().replace('</script', '<\\/script') + '</script>')
    html = html.replace('</body>', ''.join(scripts) + '</body>')
    for asset in ASSETS.glob('*.svg'):
        html = html.replace('/assets/' + asset.name, 'data:image/svg+xml;base64,' + base64.b64encode(asset.read_bytes()).decode())
    return {'uri': URI, 'mimeType': MIME, 'text': html, '_meta': {
        'ui': {'prefersBorder': False, 'csp': {'connectDomains': [], 'resourceDomains': []}},
        'openai/widgetDescription': 'Codex 项目总控台：项目、未读结果与关联待办。',
        'openai/widgetPrefersBorder': False,
        'openai/widgetCSP': {'connect_domains': [], 'resource_domains': []},
    }}
