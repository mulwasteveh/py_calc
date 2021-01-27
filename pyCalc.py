#defining an addition function
def Add(a,b):
    return a+b

#defining a substraction function
def subtract(a,b):
    return a-b

#defining a multiplication function
def Multiply(a,b):
    return a*b

#defining a division function
def divide(a,b):
    return a/b

print("select options:")
print("1.Add")
print("2.subtract")
print("3.multiplily")
print("4.divide")

choice = input("Enter your choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", Add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", Multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")