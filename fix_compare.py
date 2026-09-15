from pathlib import Path
p=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html')
s=p.read_text().replace("$('compareLine').style.left=v+'%';","")
p.write_text(s)
print('comparison fixed')
