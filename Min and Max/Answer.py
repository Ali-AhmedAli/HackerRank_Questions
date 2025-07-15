import numpy

n,m = map(int,input().split(" "))
arr = []
l = []
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))
l = numpy.min(arr,axis=1)
print(numpy.max(l))
