def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == "__main__":
    try:
        inp = int(input("Enter a digit: "))
        print(fact(inp))

    except ValueError:
        print("Value Error")
