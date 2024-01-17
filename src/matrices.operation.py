import numpy as np
import music21 as music
import math

x = np.ones((2,3,4))
y = np.ones((2,3,4))

z = x + y
print(z)
z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)
z = 2*x / np.exp(y)
print(z)

print(x.T, y.T)
x = np.ones((2,3,4))
y = np.ones((2,4,3))

z = np.dot(x, y)
#z = x @ y.T
print(z, z.shape)

a = np.arange(3*4*5*6).reshape((3,4,5,6))
b = np.arange(3*4*5*6)[::-1].reshape((4,5,6,3))
#print(a,b)
#np.dot(a, b)[2,3,2,1,2,2]
#print(np.dot(a, b))
499128
sum(a[2,3,2,:] * b[1,2,:,2])
499128