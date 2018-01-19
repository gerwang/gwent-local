width=650
height=800
from PIL import Image
import os
for filename in os.listdir('.'):
    if filename.endswith('.png'):
        image=Image.open(filename)
        new_image=Image.new('RGBA',(width,height))
        new_image.paste(image,(new_image.width-image.width,
                               new_image.height-image.height))
        image.save('./original/'+filename,'PNG')
        new_image.save(filename,'PNG')
