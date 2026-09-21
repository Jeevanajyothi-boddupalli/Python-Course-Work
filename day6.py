#simple if
n = -5
if n > 0:
   print('+ve')
else:
   print('-ve')

#if else
age = int(input())
if age >= 18:
   print("you are eligible for voting")
else:
   print("you are not eligible")

#if elif
marks = int(input())
if marks > 90:
    print('A')
elif marks > 75:
    print('B')
elif marks > 50:
    print('c')
elif marks > 35:
    print('D')
else:
    print('Fail')

#nested if
a = 10
b = 20
c = 15
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)