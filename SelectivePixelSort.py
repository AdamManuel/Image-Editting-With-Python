from PIL import Image
from PIL import ImageColor

Selection = Image.open(input("Selection file name - "), "r")
Picture = Image.open(input("Image file name - "), "r")
pixelSelection = Selection.load()
pixeltoSort = Image.new("r", Picture.size(), color= ImageColor("white"))
