def value():
    num1 = int(input("the 1st no. : "))
    num2 = int(input("the 2nd no. : "))  
    return num1 , num2

def operation():
    operator = input("choose operator: +, -, *, /, %: ")
    return operator
while True:
    while True:
        operator = operation()
        if operator in ('+', '-', '*', '/', '%'):
            break
        else:
            print("Syntax error! Please choose a valid operator: +, -, *, /, %\n")

    while True:
        num1, num2 = value()
        if operator in ('/', '%') and num2 == 0:
            print("Invalid syntax: Divisor can't be zero. Please reconsider the data.\n")
        else:
            break


    if(operator == '+'):
        print(f"{num1}+{num2}=", num1 + num2)
    elif(operator == '-'):
        print(f"{num1}-{num2}=", num1 - num2)
    elif(operator == '*'):
        print(f"{num1}*{num2}=", num1 * num2)
    elif(operator == '/'):
        print(f"{num1}/{num2}=", num1 / num2)
    elif(operator == '%'):
        print(f"{num1}%{num2}=", num1 % num2)
    else:
        print("something went wrong/synatx error")

    again = input("calculate again? (yes/no): ").strip().lower()
    if(again != 'yes'):
        print("have a good day")
        break