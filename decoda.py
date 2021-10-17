from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/aajib/PycharmProjects/ADVANCED PROJECT/MYname23234.jpg')

result = decode(img)


print(result)
