# patternprint
M = [[1,2,3],[4,5,6],[7,8,9]]
for row in range(3):
    for column in range(3):
        print(M[row][column], end=" ")
    print()

# star pattern 
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()
for row in range(4):
    for column in range(4):
        print("*", end=" ")
    print()

# diagonal pattern
for r in range(4):
    for c in range(4):
        if r == c or (r + c) == 3:
           print("*", end=" ")
        else:
           print(" ", end=" ")
    print()

for r in range(4):
    for c in range(4):
        if (r+c) % 2 == 0:
           print("1", end=" ")
        else:
           print("0", end=" ")
    print()

# even,odd
for r in range(1,5):
    for c in range(1,5):
        if r % 2 == 0:
            print("odd", end=" ")
        else:
            print("even", end=" ")
    print()