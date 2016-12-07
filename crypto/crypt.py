import math, random
from crypto.algorithms import ChaoticBakerMap, EllipticCurve, DPRE
from crypto.helper import Image

def encrypt(data):
    key = [2**e for e in range(1, int(math.log(len(data), 2)))]
    key = key[::-1] + [2]
    random.shuffle(key)
    cbm = ChaoticBakerMap.encrypt(data, key)
    Image.save('cbm-im.jpg', cbm)
    ecc = EllipticCurve.encrypt(cbm)
    Image.save('cbm-ecc-im.jpg', ecc)
    dpre = DPRE.encrypt(ecc)
    Image.save('cbm-ecc-dpre-im.jpg', dpre)

def decrypt(data, key):
    return (key, ChaoticBakerMap.decrypt(data, key))