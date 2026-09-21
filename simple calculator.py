def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
    choice = input("Choose (1-5): ")

    if choice == '5':
        print("Bye Sai!")
        break

    if choice in ('1', '2', '3', '4'):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Answer = {add(n1, n2)}")
        elif choice == '2':
            print(f"Answer = {sub(n1, n2)}")
        elif choice == '3':
            print(f"Answer = {mul(n1, n2)}")
        elif choice == '4':
            if n2 == 0:
                print("Zero tho divide cheyalemu!")
            else:
                print(f"Answer = {div(n1, n2)}")
    else:
        print("Wrong choice!")