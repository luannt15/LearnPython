def add(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
    
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
option = input("Enter the operation +, -, *, / :")

if option == '+':
    print(number_1, "+", number_2, "=", add(number_1, number_2))
  
elif option == '-':
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
  
elif option == '*':
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
  
elif option == '/':
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
    
else:
    print("Invalid input")