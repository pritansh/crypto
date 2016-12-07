# crypto

## Importing

```python
import crypto as crp
``` 

## Algorithms

### Chaotic Baker Map

```python
import math, random, crypto.algorithms as crpalg, numpy as np

l = np.array([e for e in range(1, 65)]).reshape(8, 8)
print(l)

array([[ 1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16],
       [17, 18, 19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30, 31, 32],
       [33, 34, 35, 36, 37, 38, 39, 40],
       [41, 42, 43, 44, 45, 46, 47, 48],
       [49, 50, 51, 52, 53, 54, 55, 56],
       [57, 58, 59, 60, 61, 62, 63, 64]])

key = [2**e for e in range(1, int(math.log(len(l), 2)))]
key = key[::-1] + [2]
random.shuffle(key)
print(key)

[2, 4, 2]

e = crpalg.ChaoticBakerMap.encrypt(l, key)
print(e)

([2, 4, 2], array([[31, 23, 15,  7, 32, 24, 16,  8],
       [63, 55, 47, 39, 64, 56, 48, 40],
       [11,  3, 12,  4, 13,  5, 14,  6],
       [27, 19, 28, 20, 29, 21, 30, 22],
       [43, 35, 44, 36, 45, 37, 46, 38],
       [59, 51, 60, 52, 61, 53, 62, 54],
       [25, 17,  9,  1, 26, 18, 10,  2],
       [57, 49, 41, 33, 58, 50, 42, 34]]))

d = crpalg.ChaoticBakerMap.decrypt(e[1], e[0])
print(d)

([2, 4, 2], array([[ 1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16],
       [17, 18, 19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30, 31, 32],
       [33, 34, 35, 36, 37, 38, 39, 40],
       [41, 42, 43, 44, 45, 46, 47, 48],
       [49, 50, 51, 52, 53, 54, 55, 56],
       [57, 58, 59, 60, 61, 62, 63, 64]]))
```

## Helper

### Point

```python
import crypto.helper as crphlp

p1 = crphlp.Point.toPoint(2)
print(p1)

(-1.44225,2.0)

p2 = crphlp.Point.toPoint(7)
print(p2)

(3.476027,7.0)

padd = p1 + p2
print(padd)

(-1.000268,-2.449325)

psub = p1 - p2
print(psub)

(1.314791,3.045135)

pdbl = p1 * 2
print(pdbl)

(5.318295,-12.546875)

pmul = p1 * 8
print(pmul)

(-1.473748,1.949132)
```