if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        x = input()
        if "pop" in x :
            s.pop()
        elif "remove" in x :
            y = int(x[-1])
            s.remove(y)
        elif "discard" in x:
            y = int(x[-1])
            s.discard(y)
    print(sum(s))
