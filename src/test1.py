from keras.utils import to_categorical
import numpy as np
import keras
from keras.layers import Bidirectional, Concatenate, Permute, Dense, Input, LSTM, Lambda
from keras.models import Model

def dataset_test():
    print(list(zip(list('abcdefg'), list(range(3)), list(range(4)))))

    human_vocab = set()

    h = tuple('this is test string.')

    human_vocab.update(tuple(h))

    print(human_vocab)

    h_t = list(zip(sorted(human_vocab) + ['<unk>', '<pad>'], 
                     list(range(len(human_vocab) + 2))))
    print(h_t)
    human = dict(h_t)    

    print(human)

    inv_machine = dict(enumerate(sorted(human_vocab)))
    print(inv_machine)

def lambda_test():
    X = [[1,2,3,0,2],[0,0,0,0,0]]

    X = np.array(X)

    print(X.shape)
    #print(np.array(list(list(X))))

    print(np.array(list(map(lambda x : np.eye(5,5,k=0), X))))

    #l = lambda x: to_categorical(x, num_classes=5), X
    #print(l)

def dot_test():
    a = np.ones((10,30,30))
    alpha = np.ones((11,30,1))

    c = a.dot(alpha)
    print(c.shape)

    x = np.ones((10, 30, 64))
    y = np.ones((10, 30, 1))
    r = keras.layers.Dot(axes = 1)([y, x])
    print(r.shape)

lmb_layer = Lambda(lambda x: [x/2, x*2])
fc_layer = Dense(30)

def print_node_info(layer):
    for node in layer._inbound_nodes:
        print(node)
        if type(node.output_tensors) == list:
            for tensor in node.output_tensors:
                print(tensor)
        else:
            print(node.output_tensors)
            
def keras_layer_test():
    inp1 = Input((10,))
    inp2 = Input((20,))
    inp3 = Input((30,))

    print_node_info(lmb_layer)
    a1, b1 = lmb_layer(inp1)
    print_node_info(lmb_layer)
    a2, b2 = lmb_layer(inp2)
    print_node_info(lmb_layer)
    a3, b3 = lmb_layer(inp3)
    print_node_info(lmb_layer)

    d1 = Dense(10)(a1)
    d2 = Dense(20)(b1)
    d3 = Dense(30)(a2)
    d4 = Dense(40)(b2)
    
    s = a3
    for n in range(10):
        print_node_info(fc_layer)
        s = fc_layer(s)
    d5 = Dense(50)(s)

    model = Model(inputs=[inp1, inp2, inp3], outputs=[d1, d2, d3, d4, d5])
    model.summary()

if __name__ == '__main__':
    keras_layer_test()
    #dot_test()