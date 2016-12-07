import numpy as np
from crypto.helper import Point

class ChaoticBakerMap:

    @staticmethod
    def encrypt(data, key):
        enc = np.hsplit(data, np.cumsum(key))
        arr = []
        for i in range(len(key)-1, -1, -1):
            enc[i] = np.vsplit(enc[i], enc[i].shape[1])
            enc[i] = np.fliplr(enc[i])
            enc[i] = enc[i].reshape(enc[i].shape[0], 8, order='F')
            arr.append(enc[i])
        enc = np.concatenate(tuple(arr))
        return enc

    @staticmethod
    def decrypt(data, key):
        key = key[::-1]
        dec = np.vsplit(data, np.cumsum(key))
        arr = []
        for i in range(len(key)-1, -1, -1):
            dec[i] = dec[i].reshape(key[i], -1, key[i], order='F')
            dec[i] = np.fliplr(dec[i]).reshape(-1, dec[i].shape[0])
            arr.append(dec[i])
        dec = np.hstack(tuple(arr))
        return dec