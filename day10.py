a,b,c = map(int,input().split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
elif a == b or b ==c:
    print(a)
elif a==b:
    if c > a:
      print(c)
    else:
      print(a)
elif b == c:
    if a> b:
      print(a)
else:
     print(b)
elif a == c:
    if b > a:
      print(b)
else:
    print(a)

# programme 2
a = map(int,input())
b = map(int,input())
c = map(int,input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)