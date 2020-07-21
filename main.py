#from graphics import *
# Importing Image from PIL package  
from PIL import Image 


#win = GraphWin("Image Testing", 500, 500)
#win.setBackground("white")
# creating a image object 
im = Image.open("image.jpg") 
px = im.load() 
im.show()


cordinate = x, y = 180, 79

# using getpixel method 
print (im.getpixel(cordinate)); 