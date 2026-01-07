def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total
# ----------------------------------------


num = int(input("Enter an integer larger than 1: "))
if num <= 1:
    print("Please enter an integer larger than 1.")
else:
    print(factorial(num))
