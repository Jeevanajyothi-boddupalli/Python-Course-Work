#loops
for n in range(1, 6):
    print(n)
for n in range(1, 11):
    if n % 2 == 0:
     print(n)
for i in range(100):
    print(i)
dates = [26,12,7,17,15,18,22]
for num in range(1, 6):
    print(num*num)
for i in range (len(dates)):
    if dates[i] >= 15:
          print(i)
nums = [10,2,33,24,57,378]
target = int(input("enter target:"))
for i in range(len(nums)):
    if nums[i] == target:
        print(f"found at {i}")
        break
else:
    print("not found")

#loop based problemsl
L = [90,56,3,2,15,78,97]
maximum = float('-inf')
for num in L:
    if num > maximum:
        maximum = num
        print(maximum)