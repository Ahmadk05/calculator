import math
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
# 5. SQUARE ROOT
# 6. RAISE TO A POWER OF 2


print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")
operation = input()

if operation == "1": #perform addition
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": #perform subtraction
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3": #perfrom multiplication
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The product is " + str(int(num1) * int(num2)))
elif operation == "4": #Peform division
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   print("The result is " + str(int(num1) / int(num2)))
elif operation == "5": #Peform square root
   num = int(input("Enter number: "))
   print("The squareroot is %f "  %(math.sqrt(num)) )
elif operation == "6": # Square a number
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print("The power is %d " %(pow(num1, num2)))

else:
    print("Invalid Entry")
