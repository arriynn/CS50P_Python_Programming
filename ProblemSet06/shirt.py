import sys
from PIL import Image, ImageOps
import os

if len(sys.argv)==3:
    extentions= [".jpg", ".jpeg", ".png"]
    extentions1= os.path.splitext(sys.argv[1])
    extentions2= os.path.splitext(sys.argv[2])
    if extentions1[1]== extentions2[1] and extentions1[1] in extentions:

        try: 
            user_image= Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File doesn't exist")

        shirt= Image.open("shirt.png")
        size= shirt.size

        user_image= ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
    else:
        sys.exit("Imvalid extention")
elif len(sys.argv)>3:
    sys.exit("Too many arguments")
elif len(sys.argv)<3:
    sys.exit("Too few arguments")