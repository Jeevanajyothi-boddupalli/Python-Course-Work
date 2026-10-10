# if condition
n = -5
if n > 0:
   print('+ve')
else:
   print('-ve')
print(n > 0)

#if else
age = int(input())
if age >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#if elif
marks = int(input())
if marks > 90:
    print("A")
elif marks > 75:
    print("B")
elif marks > 50:
    print("C")
elif marks > 35:
    print("D")
else:
    print("Fail")

#nested if
a,b,c = map(int,input().split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
elif a == b or b == c:
    print(a)
elif a == b:
   if c > a:
     print(c)
   else:
     print(a)
elif b == c:
    if a > b:
     print(a)
    else:
     print(b)
elif a == c:
    if b > a:
      print(b)
    else:
      print(a)
