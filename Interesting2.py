__author__ = 'Adam Manuel'
from PIL import Image

picture = Image.open("Mountains.jpg", "r")
sortedpicture = Image.open("Mountains.jpg", "r")
sorted = sortedpicture.load()
toshow = picture.load()


temp = [None]*sortedpicture.size[0]
for x in range(sortedpicture.size[1]):
    for y in range(sortedpicture.size[0]):
        temp[y] = sorted[y,x]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(sortedpicture.size[0]):
        sorted[y,x] = temp[y]
temp = [None]*sortedpicture.size[1]
for x in range(sortedpicture.size[0]):
    for y in range(sortedpicture.size[1]):
        temp[y] = sorted[x,y]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    for y in range(sortedpicture.size[1]):
        sorted[x,y] = temp[y]

for x in range(picture.size[0]):
    for y in range(picture.size[1]):
        if((toshow[x,y][0] + toshow[x,y][1] + toshow[x,y][2])/3 < 155):
            toshow[x,y] = sorted[x,y]

sortedpicture.show()
picture.show()