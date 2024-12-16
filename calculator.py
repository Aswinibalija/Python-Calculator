# Python programme to make a simple Calculator

#Function to add two numbers:
def add(x,y):
    return x+y

#Function to subtract two numbers:
def subtract(x,y):
    return x-y

#Function to multiply two numbers:
def multiply(x,y):
    return(x*y)

#Function to devide two numbers:
def divide(x,y):
    return(x/y)

#Function to get power of two numbers:
def power(x,y):
    return(x**y)

#Function to get remainder of two numbers:
def modulas(x,y):
    return(x%y)

#Function to get quotient of two numbers:
def floordevide(x,y):
    return(x//y)

print("select option: ")
print("1.add\n2.subtract\n3.multiplicateion\n4.divide\n5.power\n6.modulas\n7.floor devide")

while True:
    choice=input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4' ,'5','6','7'):
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))

        if choice=='1':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice=='2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice=='3':
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif choice=='4':
            print(num1, "/", num2, "=", divide(num1,num2))

        elif choice=='5':
            print(num1, "**", num2, "=", power(num1,num2))

        elif choice=='6':
            print(num1, "%", num2, "=", modulas(num1,num2))

        elif choice=='7':
            print(num1, "//", num2, "=", floordevide(num1,num2))

        break
    else:
        print("Invalid Choice")
















            
        
    

              
