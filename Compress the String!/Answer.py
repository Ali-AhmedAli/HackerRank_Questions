s = input()
count = 0
result = ""
for i in range(len(s)):
    count += 1
    if i == len(s)-1 or s[i] != s[i+1] :
        result += f"({count}, {s[i]}) "
        count = 0
print(result)
        
