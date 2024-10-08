#// Name: Marcus Bracken
#// Course: CIS261-Object-Oriented Computer Programming I
#// Lab: IterationAndRecursion

def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


test_numbers = [1, 5, 20, 28, 35]


print("Factorial results using an iterative function")
for number in test_numbers:
    print(f"{number}: {iterative_factorial(number)}")


print("\nFactorial results using a recursive function")
for number in test_numbers:
    print(f"{number}: {recursive_factorial(number)}")

print("Press any key to continue . . .")
