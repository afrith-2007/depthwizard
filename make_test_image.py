from PIL import Image, ImageDraw
im=Image.new('RGB',(240,180),(36,60,55))
d=ImageDraw.Draw(im); d.rectangle((80,40,160,165),fill=(200,224,204)); d.ellipse((95,15,145,65),fill=(219,160,111)); im.save('/tmp/depthwizard-test.png')
