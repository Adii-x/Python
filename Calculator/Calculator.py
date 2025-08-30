def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def remainder(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def power(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y


print("Simple Calculator")
print("==================")

while True:   # loop forever until user exits
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Power")
    print("7. Exit")   # exit option

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        print("Exiting... Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} % {num2} = {remainder(num1, num2)}")

        elif choice == '6':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid option.")
