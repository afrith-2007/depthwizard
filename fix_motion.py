from pathlib import Path
p=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html')
s=p.read_text().replace("if(fly.device)return;fly.motionX", "if(!fly.device)return;fly.motionX")
p.write_text(s)
print('motion fixed')
