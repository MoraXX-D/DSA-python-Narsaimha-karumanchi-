def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter a number: "))
result = factorial(number)
print("factorial of " + str(number) +
    " is " + str(result))