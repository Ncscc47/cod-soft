# Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    print(f"The result is: {num1 + num2}")
elif choice == '2':
    print(f"The result is: {num1 - num2}")
elif choice == '3':
    print(f"The result is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")