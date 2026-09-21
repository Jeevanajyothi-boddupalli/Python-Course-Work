import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def power(a,b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

while True:
    print("\n--- Sai's Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (a^b)")
    print("6. Square Root (sqrt)")
    print("7. Exit")
    
    choice = input("Choose 1-7: ")

    if choice == '7':
        print("Bye!")
        break

    if choice in ('1', '2', '3', '4', '5'):
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))

        if choice == '1':
            print(f"Result = {add(n1, n2)}")
        elif choice == '2':
            print(f"Result = {sub(n1, n2)}")
        elif choice == '3':
            print(f"Result = {mul(n1, n2)}")
        elif choice == '4':
            if n2 == 0:
                print("Error: Zero tho divide cheyalem!")
            else:
                print(f"Result = {div(n1, n2)}")
        elif choice == '5':
            # power ki 2 methods
            print(f"Result = {math.pow(n1, n2)}  (or) {n1 ** n2}")

    elif choice == '6':
        n = float(input("Number enter cheyyi (sqrt kosam): "))
        if n < 0:
            print("Error: Negative number ki sqrt radu!")
        else:
            print(f"sqrt({n}) = {math.sqrt(n)}")

    else:
        print("Invalid choice!")