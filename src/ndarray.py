import numpy as np

print(np.__version__)
arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])

print(arr, arr.shape, type(arr))

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

if __name__ == '__main__':
    create_test()