def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Cannot divide by zero."
  return a / b
  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")

if choice == '1':
  print("Result:", add(num1, num2))
elif choice == '2':
  print("Result:", subtract(num1, num2))
elif choice == '3':
  print("Result:", multiply(num1, num2))
elif choice == '4':
  print("Result:", divide(num1, num2))
else:
  print("Invalid choice!")

# SHORT REFLECTION ANSWERS
# 1. What functions did you create in your calculator program?
# - In my calculator program, the functions that I created were add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
#
# 2. What parameters did your functions use?
# - The parameters that my functions used were 'a' and 'b'.
#
# 3. What arguments were passed when the functions were called?
# - The arguments that were passed when the functions were called were num1 and num2.
#
# 4. How did your program use the returned value?
# - My program used the returned value by being printed directly with the result.
#
# 5. Why is it better to divide the calculator program into functions instead of writing everything in one long block of code?
# - It is better to divide the calculator program into functions instead of writing everything in one long block of code because it makes the code more easier to read, reusable, and easier to test.
