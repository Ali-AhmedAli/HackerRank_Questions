import numpy

n,m = map(int,input().split(" "))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split(" "))))
arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())


