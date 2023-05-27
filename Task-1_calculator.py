# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation from the following:- ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4):- ")

    # Check if choice is one of the four options or not 0
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number:- "))
            num2 = float(input("Enter second number:- "))

        except ValueError:
            print("Invalid input !")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants to do another calculation
        # break the while loop if answer is no
        next_calculation = input("Need to continue the calculation ? (yes/no):- ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input !")