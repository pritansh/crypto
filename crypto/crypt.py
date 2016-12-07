import math, random
from crypto.algorithms import ChaoticBakerMap

def encrypt(data):
    key = [2**e for e in range(1, int(math.log(len(data), 2)))]
    key = key[::-1] + [2]
    random.shuffle(key)
    return (key, ChaoticBakerMap.encrypt(data, key))

def decrypt(data, key):
    return (key, ChaoticBakerMap.decrypt(data, key))