from PIL import Image

sortedpicture = Image.open("Mountains.jpg", "r")
sorted = sortedpicture.load()


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

sortedpicture.show()