#!/usr/bin/env python3
"""Generate wordpress-embed.html using blob: URL approach."""
import base64, os

with open('opentype-variant-analyzer.html', 'rb') as f:
    html_bytes = f.read()

b64 = base64.b64encode(html_bytes).decode('ascii')

output = (
    '<!-- OpenType Variant Analyzer  WordPress Embed (blob URL approach) -->\n'
    '<!-- Paste this into a Custom HTML block. The script decodes the app and -->\n'
    '<!-- loads it via a blob: URL so the iframe gets the real page origin. -->\n'
    '<div id="ova-host"></div>\n'
    '<script>\n'
    '(function() {\n'
    '  var b64 = "' + b64 + '";\n'
    '  try {\n'
    '    var raw = atob(b64);\n'
    '    var bytes = new Uint8Array(raw.length);\n'
    '    for (var i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);\n'
    '    var blob = new Blob([bytes], {type: "text/html;charset=utf-8"});\n'
    '    var url = URL.createObjectURL(blob);\n'
    '    var f = document.createElement("iframe");\n'
    '    f.src = url;\n'
    '    f.style.cssText = "width:100%;min-height:900px;border:none;background:#fafaf8;";\n'
    '    f.allowFullscreen = true;\n'
    '    f.setAttribute("allow", "fullscreen");\n'
    '    document.getElementById("ova-host").appendChild(f);\n'
    '  } catch (err) {\n'
    '    var el = document.getElementById("ova-host");\n'
    '    if (el) el.textContent = "Error loading analyzer: " + err.message;\n'
    '  }\n'
    '})();\n'
    '</script>\n'
)

with open('wordpress-embed.html', 'w') as f:
    f.write(output)

print(f'Written {os.path.getsize("wordpress-embed.html")} bytes')
