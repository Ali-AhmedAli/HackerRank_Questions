from collections import OrderedDict

n = int(input())
counter = OrderedDict()

for _ in range(n):
    word = input()
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(len(counter))
print(" ".join(map(str, counter.values())))
