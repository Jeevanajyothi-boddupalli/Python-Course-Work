# right angle pattern
for r in range(1,5):
    for c in range(1,5):
        if c <= r:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#invert right angle
n = 3
for r in range(3):
    for c in range(n-r):
        print("@", end=" ")
    print()

#pyramid pattern
n = 3
for r in range(3):
    for c in range(n-r-1):
        print(" ", end=" ")
    for c in range(2*r+1):
        print("*", end=" ")
    print()

#invert pyramid
n = 3
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2*n-(2*i+1)):
        print("*", end=" ")
    print()

#rhombus
n = 3
for r in range(3):
    for c in range(n-r-1):
        print(" ", end=" ")
    for c in range(2*r+1):
        print("*", end=" ")
    print()
n = 2 
for r in range(n):
    for c in range(r+1):
        print(" ", end=" ")
    for c in range(2*n-(2*r+1)):
        print("*", end=" ")
    print()

#to get numbers in pyramid
n = 3
for r in range(n):
    for c in range(n-r):
        print(" ", end=" ")
    for c in range(2*r+1):
        print(r+1, end=" ")
    print()

#Hallow square
for r in range(4):
    for c in range(4):
        if r==0 or r==3 or c==0 or c==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Name printing pattern
name = "jeevana"
for i in range(1, len(name)+1):
    print(name[i-1]*1)

#for particular character
ch = 65
print(chr(ch))
print(chr(ch+10))

ch = 65
for i in range(4):
    for j in range(4):
        print(chr(ch), end=" ")
        ch += 1
    print()

#Diagonal
n = 4
def diagonal(Difference(arr)):
    n = len(arr)
D1 = primary_diagonal
