import numpy as np
#from music21 import *
import emoji
from scipy.special import softmax

import tensorflow as tf
from keras.layers import Dense

def test():
    nnx = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(nnx)

    print(np.sum(nnx, axis=0, keepdims=True))
    print(softmax(nnx,axis=0))

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

    y_tmp = np.random.randn(2,10)

    print(y_tmp)
    print(softmax(y_tmp))
    sm=softmax2(y_tmp) 
    print(softmax2(y_tmp),sm.sum(axis=0))

def softmax(x):
    #print(np.max(x))
    #print(x - np.max(x))
    e_x = np.exp(x - np.max(x))
    #print(e_x)
    return e_x / e_x.sum(axis=0)

def softmax2(x):
    e_x = np.exp(x)
    return e_x.T / e_x.sum(axis=1)

def weighted_sum():
    ty = 2
    tx = 3
    td = 5

    W = np.random.rand(ty,tx)
    H = np.random.rand(tx,td)
    print(W, '\r\n', H)

    C = W@H
    print(C)

    for i in range(ty):
        c = np.zeros((td,))
        for j in range(tx):
            print(f'--------{i}/{j}---------')
            print(W[i,j])
            print(H[j,:])
            c_ = W[i,j]*H[j,:]
            print(f"c_ = {c_}")
            c = c + c_

        print(f"c = {c} *")

def tf_concat_test():
    _x1 = np.arange(15).reshape(5, 3)
    print(_x1)

    _x2 = np.arange(10, 30).reshape(5, 4)
    print(_x2)

    layer1 = Dense(8)
    layer2 = Dense(8)

    x1 = layer1(_x1)
    x2 = layer2(_x2)

    print(layer1.weights)

    print(x1)
    print(x2)
    concatted = tf.keras.layers.Concatenate()([_x1, _x2])
    print(concatted.shape)

def tf_dot_test():
    x = np.arange(10).reshape(1, 5, 2)
    print(x)
    y = np.arange(10, 20).reshape(1, 2, 5)
    print(y)
    
    print(x@y)
    print(y@x)

    xy = tf.keras.layers.Dot(axes=(1, 2))([x, y])
    print(xy)


    _x1 = np.arange(10).reshape(5, 2)
    _x2 = np.arange(10, 20).reshape(5, 2)
    x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
    x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
    print(_x1, _x2)
    dotted = tf.keras.layers.Dot(axes=1)([_x1, _x2])
    print(dotted, dotted.shape)

from keras.models import Sequential
from keras.layers import RepeatVector

def keras_test():
    model = Sequential()
    model.add(Dense(32, input_dim=32))
    # now: model.output_shape == (None, 32)
    # note: `None` is the batch dimension
    model.summary()

    model.add(RepeatVector(3))
    # now: model.output_shape == (None, 3, 32)
    model.summary()
    
if __name__ == "__main__":
    #test()
    #weighted_sum()
    keras_test()