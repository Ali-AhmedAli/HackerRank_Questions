import numpy

n,m,p = map(int,input().split(" "))
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int,input().split(" "))))
for _ in range(m):
    arr2.append(list(map(int,input().split(" "))))
# arr = numpy.array(arr)
print(numpy.concatenate((arr1, arr2), axis = 0))
