import crypto as crp
import numpy as np

l = np.array([e for e in range(1, 65)]).reshape(8, 8)
print(l)

e = crp.encrypt(l)
print(e)

d = crp.decrypt(e[1], e[0])
print(d)