file= input("File name: ").lower()

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg"):
    print("image/jpg")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image.png")
elif file.endswith(".txt"):
    print("text/txt")
elif file.endswith(".pdf"):
    print("application/pdf")
else:
    print()