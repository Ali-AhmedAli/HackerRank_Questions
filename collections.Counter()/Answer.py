if __name__ == "__main__" : 
    x = int(input())
    result = 0
    size_list = list(map(str,input().split(" ")))
    n = int(input())
    for i in range(n):
        size,price = input().split(" ")
        if size in size_list:
            result += int(price)
            size_list.remove(size)
    print(result)

