import numpy as np
#from music21 import *
import emoji

print(emoji.emojize('Python is :red_heart:'))

str = 'this is a test String.'

words = str.lower().split()

x = np.random.randn(3, 10, 4)
print(x)

a = np.ones([5,])
b = np.ones(10)
print(np.dot(a,b))
""" for n in range(4):
    print(x[:,:,n])
 """
for n in range(10):
    print(x[:,n,:])    

w_ya = np.ones([2,5])
a = np.ones((5,10))
b_y = 2*np.ones((2,1))
print(b_y)
y_hat = w_ya@a + b_y

print(y_hat)

def softmax(x):
    #print(np.max(x))
    #print(x - np.max(x))
    e_x = np.exp(x - np.max(x))
    #print(e_x)
    return e_x / e_x.sum(axis=0)

def softmax2(x):
    e_x = np.exp(x)
    return e_x.T / e_x.sum(axis=1)

y_tmp = np.random.randn(2,10)

print(y_tmp)
print(softmax(y_tmp))
sm=softmax2(y_tmp) 
print(softmax2(y_tmp),sm.sum(axis=0))