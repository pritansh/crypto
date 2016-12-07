import crypto as crp
from crypto.helper import Image

arr = Image.read('new-image.jpg')
print(arr)

crp.encrypt(arr)