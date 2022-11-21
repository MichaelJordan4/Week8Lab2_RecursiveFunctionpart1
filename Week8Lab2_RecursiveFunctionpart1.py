#Michael Jordan
#CIS261
#Week8Lab2 Fibonacci Recursive Function


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    for i in range(16):
        print(fibonacci(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()

