import numpy as np

#print(np.__version__)
#arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
#print(arr, arr.shape, type(arr))

def create_test():
    arr = np.array(['5','6','7'],ndmin=0)
    print(arr, arr.ndim, arr.shape, type(arr), arr.dtype)
    data = arr[1]
    print(data, type(data))

    print(10*'-')
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    arr_ = arr.reshape(2, 4)
    print(arr_.base)

    print(arr_, arr)
    arr_[0,1] = 11
    print(arr_, arr)
    print(arr_.base)

    print(np.eye(6, k=4, dtype=int))

from transformers import DistilBertTokenizerFast
from transformers import DistilBertForQuestionAnswering

text = ['The garden is north of the bathroom. The hallway is south of the bathroom.', 'What is north of the bathroom? These']
def tokenizer_test():
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-cased')
    encoding = tokenizer(text[1], text[0], truncation=True, padding=True, max_length=tokenizer.model_max_length)
    print(encoding.input_ids)

    pytorch_model = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-cased")

if __name__ == '__main__':
    tokenizer_test()