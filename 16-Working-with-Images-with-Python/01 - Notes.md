# Working with Images with Python
***
***
# Working with Images with Python
* The pillow library is a **fork of the PIL (Python Imaging Library) library**
```
pip install pillow
```
* pillow.readthedocs.io
## Open an image
```
from PIL import Image
mac = Image.open('example.jpg')
mac.show() # or mac in Jupyter 
```
## Image info
```
# (width, height)
mac.size
mac.filename
# return ex: 'JPEG (ISO 10918)'
mac.format_description 
```

## Crop images
* (x, y, w, h) are measured from the top left corner of the image - all 4 of these values are coordinates!
```
mac.crop((0,0,100,100))
# or
pencils = Image.open("pencils.jpg")
pencils.show()
pencils.size
```
* more:
```
# Start at top corner (0,0)
x = 0
y = 0

# Grab about 10% in y direction , and about 30% in x direction
w = 1950/3
h = 1300/10

pencils.crop((x,y,w,h))
pencils.show()
```
* more - from the bottom:
```
pencils.size
x = 0 
y = 1100
w = 1950/3
h = 1300
pencils.crop((x,y,w,h))
```
* more - getting an image close to the bottom center:
```
mac.size
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac.crop((x,y,w,h))
mac.show()
```
## Copying and pasting images
* copy with copy()
* paste with paste()
```
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))
mac # to show
mac.paste(im=computer,box=(796,0))
```
* notice how the copy is grabbed with a crop then pasted with ```paste()```

## Resizing
```
mac.size
h,w = mac.size
new_h = int(h/3)
new_w = int(w/3)
# Note this is not permanent change
# for permanent change, do a reassignment
# eg mac = mac.resize((100,100))
mac.resize((new_h,new_w))
# stretch and squeeze
mac.resize((3000,500))
```
## Rotating images
```
pencils.rotate(90)
pencils.rotate(90,expand=True)
# The image is cut off
pencils.rotate(120)
```

## Transparency
* 0 == completely transparent
* 255 == completely opaque
```
red = Image.open('red_color.jpg')
red.putalpha(128) # now has some transparency 
```
* copying an image over another with some transparency:
```
blue.paste(red,box=(0,0),mask=red)
blue # now shows as more purple / blue and red
```
* more infor on transparency: https://pillow.readthedocs.io/en/stable/

## Saving Images
```
blue.save("purple.png")
purple = Image.open("purple.png")
purple # to see it
```