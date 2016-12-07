import os, random, numpy as np
from crypto.helper import Point, Base

class ChaoticBakerMap:

    @staticmethod
    def encrypt(data, key):
        enc = np.hsplit(data, np.cumsum(key))
        arr = []
        for i in range(len(key)-1, -1, -1):
            enc[i] = np.vsplit(enc[i], enc[i].shape[1])
            enc[i] = np.fliplr(enc[i])
            enc[i] = enc[i].reshape(enc[i].shape[0], len(data), order='F')
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

class EllipticCurve:

    G = Point.getGenerator()
    nA = 97061
    Pa = G * nA
    nB = 65051
    Pb = G * nB 
    k = random.randint(21, 301)
    kG = G * k
    kGnB = kG * nB
    kPb = Pb * k

    @staticmethod
    def encrypt(data):
        length = len(data)
        data = data + 2
        data = data.reshape(-1)
        groups = len(data)/63
        data = np.concatenate((data, [0 for e in range(len(data) - 63*groups, 63)]))
        groups += 1
        k = [63*e for e in range(1, groups+1)]
        enc = np.hsplit(data, k)
        Pm = np.array([Point(63, 0) for e in range(0, groups)], dtype='object')
        for i in range(0, groups):
            Pm[i].y = Base.toBase(enc[i], 258)
            Pm[i] = EllipticCurve.kPb + Pm[i]
        Pc = np.array([e.y for e in Pm], dtype='object')
        for i in range(0, groups):
            Pc[i] = Base.fromBase(Pc[i], 256)
            if len(Pc[i]) < 63:
                pad = 63 - len(Pc[i])
                Pc[i] = np.concatenate(([0 for e in range(0, pad)], Pc[i]))
        Pc = np.array(np.hstack(Pc))
        Pc = Pc[:length**2].reshape(length, length)
        return Pc

    @staticmethod
    def decrypt(data):
        length = len(data)
        data = data.reshape(-1)
        groups = len(data)/63
        data = np.concatenate((data, [0 for e in range(len(data) - 63*groups, 63)]))
        groups += 1
        k = [63*e for e in range(1, groups+1)]
        enc = np.hsplit(data, k)
        Pm = np.array([Point(63, 0) for e in range(0, groups)], dtype='object')
        for i in range(0, groups):
            Pm[i].y = Base.toBase(enc[i], 256)
            Pm[i] = EllipticCurve.kGnB - Pm[i]
        Pc = np.array([e.y for e in Pm], dtype='object')
        for i in range(0, groups):
            Pc[i] = Base.fromBase(Pc[i], 258)
        Pc = np.array(np.hstack(Pc))
        Pc = Pc[:length**2].reshape(length, length)
        Pc = Pc - 2
        return Pc

class DPRE:

    i1 = np.array(bytearray(os.urandom(65536))).reshape(256, 256)
    i2 = np.array(bytearray(os.urandom(65536))).reshape(256, 256)

    @staticmethod
    def encrypt(data):
        img1 = data * DPRE.i1
        fft = np.fft.fft2(img1)
        fftshift = np.fft.fftshift(fft)
        img2 = fftshift * DPRE.i2
        ifftshift = np.fft.ifftshift(img2)
        ifft = np.fft.ifft2(ifftshift)
        enc = np.abs(ifft)
        return enc