# crypto

## Importing

```python
import crypto as crp
``` 

## Test

    python test.py


## Algorithms

### Chaotic Baker Map

```python
import math, random
from crypto.algorithms import ChaoticBakerMap
from crypto.helper import Image

#Reads image pixel data
arr = Image.read('new-image.jpg')
print(arr)

array([[137, 135, 133, ..., 145, 147, 114],
       [137, 137, 133, ..., 144, 148, 114],
       [138, 133, 134, ..., 133, 125,  87],
       ...,
       [ 28,  29,  28, ...,  53,  61,  59],
       [ 20,  24,  25, ...,  64,  70,  65],
       [ 22,  30,  25, ...,  71,  67,  72]], dtype=uint8)

#Generate key
key = [2**e for e in range(1, int(math.log(len(arr), 2)))]
key = key[::-1] + [2]
random.shuffle(key)
print(key)

[128, 2, 4, 2, 64, 32, 8, 16]

#Encrypt data using Chaotic Baker Map
enc = ChaoticBakerMap.encrypt(arr, key)
print(enc)

array([[ 60,  90, 105, ...,  87, 114, 114],
       [ 27,  28,  28, ...,  19,  21,  32],
       [ 30,  24,  24, ...,   6,   7,  16],
       ...,
       [ 25,  25,  34, ..., 102, 100, 105],
       [ 28,  24,  29, ...,  98, 102, 102],
       [ 22,  20,  30, ...,  93,  99,  99]], dtype=uint8)

#Decrypt using Chaotic Baker Map
dec = ChaoticBakerMap.decrypt(enc, key)
print(dec)

array([[137, 135, 133, ..., 145, 147, 114],
       [137, 137, 133, ..., 144, 148, 114],
       [138, 133, 134, ..., 133, 125,  87],
       ...,
       [ 28,  29,  28, ...,  53,  61,  59],
       [ 20,  24,  25, ...,  64,  70,  65],
       [ 22,  30,  25, ...,  71,  67,  72]], dtype=uint8)
```

### Elliptic Curve Cryptography

```python
from crypto.algorithms import EllipticCurve
from crypto.helper import Image

#Reads image pixel data
arr = Image.read('new-image.jpg')
print(arr)

array([[137, 135, 133, ..., 145, 147, 114],
       [137, 137, 133, ..., 144, 148, 114],
       [138, 133, 134, ..., 133, 125,  87],
       ...,
       [ 28,  29,  28, ...,  53,  61,  59],
       [ 20,  24,  25, ...,  64,  70,  65],
       [ 22,  30,  25, ...,  71,  67,  72]], dtype=uint8)

#Encrypt data using Elliptic Curve Cryptography
enc = EllipticCurve.encrypt(arr)
print(enc)

array([[7L, 230L, 36L, ..., 221L, 40L, 169L],
       [253L, 161L, 86L, ..., 80L, 68L, 175L],
       [248L, 72L, 111L, ..., 242L, 6L, 173L],
       ...,
       [10L, 211L, 103L, ..., 223L, 101L, 92L],
       [53L, 246L, 88L, ..., 242L, 166L, 152L],
       [70L, 83L, 219L, ..., 116L, 198L, 63L]], dtype=object)
```

### Double Phase Random Encryption (DPRE)

```python
from crypto.algorithms import DPRE
from crypto.helper import Image

#Reads image pixel data
arr = Image.read('new-image.jpg')
print(arr)

array([[137, 135, 133, ..., 145, 147, 114],
       [137, 137, 133, ..., 144, 148, 114],
       [138, 133, 134, ..., 133, 125,  87],
       ...,
       [ 28,  29,  28, ...,  53,  61,  59],
       [ 20,  24,  25, ...,  64,  70,  65],
       [ 22,  30,  25, ...,  71,  67,  72]], dtype=uint8)

#Encrypt data using DPRE
enc = DPRE.encrypt(arr)
print(enc)

array([[ 39184.79236544,  31558.21415737,  10254.31990452, ...,
         24183.83751755,  28532.98564661,  12211.39153403],
       [ 17431.01848867,  25974.26246758,  11413.47217687, ...,
         31950.20943769,   6424.28396344,  11303.68433828],
       [ 16675.71377409,  20608.41715477,  20999.77408024, ...,
         32157.42918628,   7109.34499225,  28436.10538492],
       ...,
       [ 27190.09935674,  12959.63110726,  19204.22515069, ...,
         26776.17019205,  20199.51902081,  11545.19270325],
       [ 30221.31521539,  16714.42468642,  15754.56026733, ...,
         18674.96264633,  23839.93259786,  34145.27576264],
       [ 21330.89385981,  18660.61295716,  36930.08247056, ...,
         32991.09714542,  32817.97151161,  14057.67015299]])
```

## Helper 

### Base

```python
import numpy as np
from crypto.helper import Base

#Convert list of base 2 to integer
dec = Base.toBase(np.array([1, 0, 1, 1]), 2)
print(dec)

11

#Convert integer to list of base 2
bin = Base.fromBase(dec, 2)
print(bin)

array([1, 0, 1, 1], dtype=object)
```

### Image

```python
from crypto.helper import Image

#Reads image pixel data
arr = Image.read('new-image.jpg')
print(arr)

array([[137, 135, 133, ..., 145, 147, 114],
       [137, 137, 133, ..., 144, 148, 114],
       [138, 133, 134, ..., 133, 125,  87],
       ...,
       [ 28,  29,  28, ...,  53,  61,  59],
       [ 20,  24,  25, ...,  64,  70,  65],
       [ 22,  30,  25, ...,  71,  67,  72]], dtype=uint8)

#Saves image pixel data
Image.save('new-image.jpg', arr)
```