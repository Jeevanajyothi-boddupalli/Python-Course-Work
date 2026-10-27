#while loop
i = 5
while i >= 1:
    print(i, end=" ")
    i = i - 1
else:
    print("loop complete")

#while w.t else
n = int(input("Enter number: "))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print(total)
    

#2nd
i = 1 
while i < 10:
#if i == 5
#break  
    print(i, end = " ")
    i = i + 1
else:
    print("loop complete")

#3rd
n = 2016
print(n % 10)
print(n // 10)
#counting the numbers of digits in a given number
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

#with string
n = 234
string = str(n)
print(type(n))
print(type(string))

#2nd
n = 234
total = 0
string = str(n)
for num in string:
    total = total + int(num)
print(total)