from pathlib import Path
p=Path('/home/ubuntu/projects/depthwizard-b61638c4/index.html')
s=p.read_text()
old="$('demoBtn').onclick=()=>{const svg=`<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1200\" height=\"800\"><rect width=\"100%\" height=\"100%\" fill=\"#243c37\"/><path d=\"M0 650L420 380 760 620 1200 300V800H0Z\" fill=\"#3f6654\"/><circle cx=\"600\" cy=\"290\" r=\"90\" fill=\"#dba06f\"/><path d=\"M500 390h210l110 410H390z\" fill=\"#c8e0cc\"/></svg>`;const f=new File([svg], 'sample-subject.svg',{type:'image/svg+xml'});const r=new FileReader();r.onload=()=>{const blob=new Blob([svg],{type:'image/svg+xml'});const file=new File([blob],'sample-subject.svg',{type:'image/svg+xml'});choose(file);processFile(file)};r.readAsText(f)};"
new="$('demoBtn').onclick=()=>{const svg=`<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1200\" height=\"800\"><rect width=\"100%\" height=\"100%\" fill=\"#243c37\"/><path d=\"M0 650L420 380 760 620 1200 300V800H0Z\" fill=\"#3f6654\"/><circle cx=\"600\" cy=\"290\" r=\"90\" fill=\"#dba06f\"/><path d=\"M500 390h210l110 410H390z\" fill=\"#c8e0cc\"/></svg>`;const img=new Image();img.onload=()=>{const c=document.createElement('canvas');c.width=1200;c.height=800;c.getContext('2d').drawImage(img,0,0);c.toBlob(blob=>{const file=new File([blob],'sample-subject.png',{type:'image/png'});choose(file);processFile(file)},'image/png')};img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg)};"
if old not in s: raise SystemExit('old demo block not found')
p.write_text(s.replace(old,new))
print('patched')

def main(): pass
