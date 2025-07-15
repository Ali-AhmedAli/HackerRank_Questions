import numpy

n,m = map(int,input().split(" "))
arr = []
l = []
result = 0
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))
l = (numpy.sum(arr, axis = 0))
print(numpy.prod(l))
