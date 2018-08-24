#Rotate the image
from PIL import Image
img = Image.open("smaple1.jpg")
#Display origional image
img.show()
#Actutal code
img_rotate = img.rotate(-90)
img_rotate.show()
#convert image into greyscale
img = Image.open('smaple1.jpg').convert('LA')
img.save('greyscale.png')
img.show()
#create a thumbnail
size = (75,75)
img = Image.open('smaple1.jpg')
img.thumbnail(size)
img.save('thumbnail.jpg')
img.show()
#crop the image
img = Image.open('smaple1.jpg')
width, height = img.size
left = (width- 128)//2
top = (height - 128)//2
right = (width - 128)//2
bottom = (height - 128)//2
img.crop((left, top, right, bottom))
img.save('img_crop.jpg')
img.show()