import numpy as np
arr = np.array([1,2,3,4,5])
marks = [65,76,83,70,50]
marks_array = np.array(marks)
print(marks_array)
print(arr)

#dimensions
print(arr.ndim)
arr2 = np.array([[1,2,3]
                 [4,5,6]
                 [7,8,9]])
print(arr2.ndim)

#no.of rows & columns
print(arr.shape)
print(arr2.shape)

#type
print(arr.dtype)
print(arr2.dtype)

#no.of elements
print(arr.size)
print(arr2.size)

#3D array 
arr3 = np.array([[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]])
