from pathlib import Path
import re
html=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html').read_text()
scripts=re.findall(r'<script>(.*?)</script>', html, flags=re.S)
Path('/tmp/depthwizard_client.js').write_text(scripts[-1])
print('scripts',len(scripts),'client_bytes',len(scripts[-1]))
