if __name__ == '__main__':
    dic = {}
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name] = score
    l = list(set(dic.values()))
    l.sort()
    for i in dic.keys():
        if dic[i] == l[1]:
            result.append(i)
    result.sort()
    print("\n".join(result))
