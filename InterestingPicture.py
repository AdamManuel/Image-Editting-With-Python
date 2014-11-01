__author__ = 'Adam Manuel'
from PIL import Image

picture = Image.open("Thing.jpg", "r")
toshow = picture.load()



temp = [None]*picture.size[0]
for x in range(picture.size[1]):
    for y in range(picture.size[0]):
        temp[y] = toshow[y,x]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(picture.size[0]):
        if((toshow[y,x][0] + toshow[y,x][1] + toshow[y,x][2])/3 < 155):
            toshow[y,x] = temp[y]

temp = [None]*picture.size[1]
for x in range(picture.size[0]):
    for y in range(picture.size[1]):
        temp[y] = toshow[x,y]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(picture.size[1]):
        if((toshow[x,y][0] + toshow[x,y][1] + toshow[x,y][2])/3 < 155):
            toshow[x,y] = temp[y]
picture.show()