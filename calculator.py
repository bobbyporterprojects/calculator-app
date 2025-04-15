def add(x, y):
    addition = x + y
    return addition

def subtract(x, y):
    subtraction = x - y
    return subtraction

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return None
    

while True:
    try:
        operation = input("Please enter choice of operation (+-*/): ")
        number1 = int(input("Please enter first number: "))
        number2 = int(input("Please enter second number: "))
        if operation == "+":
            result  = add(number1, number2)
        elif operation == '-':
            result  = subtract(number1, number2)
        elif operation == '*':
            result  = multiply(number1, number2)
        elif operation == '/':
            result  = divide(number1, number2)
        print(result)
        new_choice = input('Would you like to perform another calcuation? (y/n): ')
        if new_choice.lower() != 'y':
            print("Goodbye")
            break
    except Exception:
            print("Error occured")
            
#test commit 
#test commit 2
