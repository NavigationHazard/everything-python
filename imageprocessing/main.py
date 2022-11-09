
from PIL import Image, ImageFilter

im = Image.open("./images/Screenshot 2022-11-09 at 7.26.57 PM.png")

blurim = im.filter(ImageFilter.SMOOTH)
blurim.save("blur.png", 'png')
jpim = blurim.convert('L')
jpim.save('grren.png' , 'png')
im.thumbnail((400, 200))
im.save('image.png')
