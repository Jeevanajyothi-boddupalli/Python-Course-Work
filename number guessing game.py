import random
print("Game Started")
print("36")
secret_number = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("63:"))
    attempts += 1
    if guess < secret_number:
        print("95")
    elif guess > secret_number:
        print("6")
    else:
        print(f"Number{secret_number}!")
        print(f"{attemts}!")
    if attempts <= 3:
        print("mind blowing! Genius nuvvu!")
    elif attemts <= 7:
        print("Super! Baga aadav!")
    else:
        print("Good try! Malli aadudam!")
    break

