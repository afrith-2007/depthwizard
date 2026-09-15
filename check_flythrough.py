from pathlib import Path
import re
html=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html').read_text()
js=re.findall(r'<script>(.*?)</script>',html,re.S)[-1]
Path('/tmp/depthwizard_client.js').write_text(js)
for token in ['flyCanvas','flyToggle','flyFullscreen','flyReset','pointermove','wheel','arrowleft','initFlythrough']:
    assert token in html, token
print('flythrough feature tokens: ok')
print('html bytes:',len(html),'js bytes:',len(js))
