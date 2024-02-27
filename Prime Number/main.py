try:
    number = int(input("Enter new number: "))
    if number < 2:
        raise ValueError("number must greater than 2")
    is_prime = True

    for i in range(2, number):
        if not number % i:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

except ValueError:
    print("Invalid data (must greater than 2)")
