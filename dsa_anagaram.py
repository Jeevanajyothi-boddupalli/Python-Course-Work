d1 = {}
d2 = {}
s = "anagram"
t = "nagaram"
for ch in s:
    if ch in d1:
        d1[ch] +=1
    else:
        d1[ch] = 1

for ch in t:
    if ch in d2:
        d2[ch] += 1
    else:
        d2[ch] = 1
if d1 == d2:
        print(True)
else:
        print(False)