n = int(input())
if n > 0:
    if n % 2 == 0:
        print("postive even")
    else:
        print("positive odd")
elif n < 0:
    if n % 2 == 0:
        print("negetive even")
    else:
        print("negative odd")
else:
    print(0)

#github problem
balance = 5000
withdrawn_amount = int(input("Enter withdraw amount: "))
if withdrawn_amount <= balance:
    balance = balance - withdrawn_amount
    print(withdrawn_amount,"has been withdrawn")
    print("your balance",balance)
else:
    print("you have no sufficient amount")

#github 2
amount = int(input("Enter amount: "))
if amount >= 2000:
    discount = amount * (20/100)
    total_amount = amount - discount
    print(total_amount)
else:
    print("no discount please pay",amount)