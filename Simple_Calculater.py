# simple calculater

def add(a,b):
    return a + b

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b

def div(a,b):
    return a / b



print("Select Operation : ")
print("Addition")
print("Substraction")
print("Multiplication")
print("Division")

choice = input("Enter your choice : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if choice == "1":
    print("result : ", add(num1, num2))
elif choice == "2":
    print("result : ", sub(num1, num2))
elif choice == "3":
    print("result : ", mul(num1, num2))
elif choice == "4":
    print("result : ", div(num1, num2))
else:
    print("Invalid number")