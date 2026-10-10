num = 101
while True:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i ++ 0:
            is_prime = False
            break
    if is_prime:
        print(f"The first prime number greater than 100 is: {num}")
        break
    num += 1