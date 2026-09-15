from pathlib import Path
import re
html=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html').read_text()
js=re.findall(r'<script>(.*?)</script>',html,re.S)[-1]
Path('/tmp/depthwizard_client.js').write_text(js)
required=['8D immersive controls','flyFrame','fly.dims','deviceMotion','compareRange','flyFullscreen','flyPlay','flyReset','pointermove','wheel','arrowleft']
for token in required:
    assert token in html, token
print('8D controls: ok')
print('HTML bytes:',len(html),'client JS bytes:',len(js))
