from PIL import Image
from PIL import ImageFilter

print("Enter the name of the image")
name = input("Name - ")

picture = Image.open(name, "r")
sortedpicture = Image.open(name, "r")
sorted = sortedpicture.load()
toshow = picture.load()

for x in range(sortedpicture.size[0]):
    temp = [None]*sortedpicture.size[1]
    for y in range(sortedpicture.size[1]):
        temp[y] = sorted[x,y]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    tempftemp = [None]*sortedpicture.size[1]
    for y in range(sortedpicture.size[1]):
        if(y%2==0):
            tempftemp[int((sortedpicture.size[1]/2)+(y/2))] = temp[sortedpicture.size[1] - (y+1)]
        else:
            tempftemp[int((sortedpicture.size[1]/2)-(y/2))] = temp[sortedpicture.size[1] - (y+1)]
    temp = tempftemp
    for y in range(sortedpicture.size[1]):
        sorted[x,y] = temp[y]


for x in range(sortedpicture.size[1]):
    temp = [None]*sortedpicture.size[0]
    for y in range(sortedpicture.size[0]):
        temp[y] = sorted[y,x]
    list.sort(temp, key=lambda color: color[0]+color[1]+color[2], reverse=True)
    tempftemp = [None]*sortedpicture.size[0]
    for y in range(sortedpicture.size[0]):
        if(y%2==0):
            tempftemp[int((sortedpicture.size[0]/2)+(y/2))] = temp[sortedpicture.size[0] - (y+1)]
        else:
            tempftemp[int((sortedpicture.size[0]/2)-(y/2))] = temp[sortedpicture.size[0] - (y+1)]
    temp = tempftemp
    for y in range(sortedpicture.size[0]):
        sorted[y,x] = temp[y]

sortedpicture = sortedpicture.filter(ImageFilter.BLUR)
sorted = sortedpicture.load()
picture = picture.filter(ImageFilter.BLUR)
toshow = picture.load()


for x in range(picture.size[0]):
    for y in range(picture.size[1]):
        if((toshow[x,y][0] + toshow[x,y][1] + toshow[x,y][2])/3 >werdfg 155):
            toshow[x,y] = sorted[x,y]

picture.save("new"+name[:4] + ".jpg", "JPEG")
picture.show()