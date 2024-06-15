#CALCULATOR
def is_float(value):
    parts=value.split('.')
    if len(parts)> 2:
        return False
    for part in parts:
        if not part.isnumeric():
            return False
    return True
a=input("Enter the first number: ")
while not is_float(a):
    a=input("Please enter valid first number: ")
b=input("Enter the second number: ")
while not is_float(b):
    b=input("Please enter valid second number: ")
check=True
while check:
    operation = input("""Please enter the operation to perform:
                  + for addition
                  - for subtraction
                  * for multiplication
                  / for division
                    """)
    if operation == '+':
        result=float(a)+float(b)
    elif operation == '-':
        result=float(a)-float(b)
    elif operation == '*':
        result=float(a)*float(b)
    elif operation == '/':
        if float(b)==0:
            print("The result is undefined")
            exit()
        result=float(a)/float(b)
    else:
        print("Please enter valid operation")
        continue
    check=False
print(f"The result is {result}")