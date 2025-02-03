import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(a) 

b = np.array([[1, 3, 4], [3, 4, 5]], dtype=int)
print(b) 
print(b.itemsize)

c = np.ones((3,4), dtype=int)
print(c)

d = np.identity(3, dtype=int)
print(d)

e = np.array([u"\u2211", u"\u220F"], dtype="U")
print(e) 

print(a + b)
print(a.max())

f = a.T
print(f)

j = np.matrix("1,0,3;-1,-1,2;4,7,2")
j_inv = np.linalg.inv(j)
print(j_inv)