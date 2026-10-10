n = int(input())
d = {}
count = 0
for i in range(n):
    word = input().strip()
    if word in d:
        d[word]+=1
    else:
        d[word] = 1
        count+=1
print(count)
print(*d.values())