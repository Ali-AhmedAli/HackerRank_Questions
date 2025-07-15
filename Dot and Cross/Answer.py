import numpy

n = int(input())
arr_a = []
arr_b = []
for _ in range(n):
    arr_a.append(list(map(int,input().split(" "))))
for _ in range(n):
    arr_b.append(list(map(int,input().split(" "))))
print(numpy.dot(arr_a, arr_b))

