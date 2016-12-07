import math, random
from crypto.algorithms import ChaoticBakerMapEncrypt, ChaoticBakerMapDecrypt

def encrypt(data):
    key = [2**e for e in range(1, int(math.log(len(data), 2)))]
    key = key[::-1] + [2]
    random.shuffle(key)
    return (key, ChaoticBakerMapEncrypt(data, key))

def decrypt(data, key):
    return (key, ChaoticBakerMapDecrypt(data, key))