import numpy as np
import music21 as music
import math

print(-np.log(1.0/27)*7)

np.random.seed(1)
ps = np.array([0.5, 0.1, 0.1, 0.3])
probs = np.array([0.1, 0.0, 0.7, 0.2])

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(aa_milne_arr, p = ps))
idx = np.random.choice([0, 1, 2, 3], p = probs)
print(idx)
print(np.random.choice(aa_milne_arr, p = probs))

matrix1 = np.array([[1,1],[2,2],[3,3]]) # (3,2)
matrix2 = np.array([[0],[0],[0]]) # (3,1) 
vector1D = np.array([1,1]) # (2,) 
vector2D = np.array([[1],[1]]) # (2,1)
print(np.dot(matrix1,vector1D))
print(matrix2)
print(np.dot(matrix1,vector1D) + matrix2)
print(10*'-')
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

c = 100*np.random.randn(5,6)
print(c)
ccc = np.ones((5,6))

cc = np.clip(c, -10, 10, out = ccc )
print(cc,c,ccc)