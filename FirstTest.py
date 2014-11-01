__author__ = 's542021'
from PIL import Image
from PIL import ImageFilter

image1 = Image.open("Truck1.jpg", "r")
image2 = Image.open("Truck2.jpg", "r")
image3 = Image.open("Skyline.png", "r")
toshow = image1.load()
toshow2 = image3.load()
sizex = image1.size[0]
sizey = image1.size[1]
#image1.show()
#image2.show()
#IDK honestly
#for x in range(sizex):
#    for y in range(sizey):
#        if((toshow[x,y][0]+toshow[x,y][1]+toshow[x,y][2])/3 > 200):
#            toshow[x,y] = toshow[sizex-(x+1), y]
#image1.show()
#wut

temp = [None]*600
for x in range(sizex):
    for y in range(sizey):
        temp[y] = toshow2[y,x]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(sizey):
        toshow2[y,x] = temp[y]
for x in range(sizex):
    for y in range(sizey):
        temp[y] = toshow2[x,y]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(sizey):
        toshow2[x,y] = temp[y]
image3.show()