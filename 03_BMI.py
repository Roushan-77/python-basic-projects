
def height_conversion():
    choice = int(input("1. feet and inch to meter\n2. cm to m\nwhat you wanna do: "))
    if(choice == 1):
        feet = int(input("feet part of your height: "))
        inch = int(input("inch part of your height: "))
        height_m = ((12 * feet + inch) * 2.54) / 100
    elif choice == 2:
        cm = float(input("Enter your height in cm: "))
        height_m = cm / 100
    else:
        print("Invalid option for height conversion.")
        return height_conversion()
    return height_m

def weight_conversion():
    weight = float(input("enter your weight in lbs: "))
    weight_kg = weight*0.453592
    return weight_kg

def BMI_calculator(height,weight):
    BMI = (weight)/(height*height)
    print(f"\nYour BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("Category: Underweight")
    elif 18.5 <= BMI < 25:
        print("Category: Normal weight")
    elif 25 <= BMI < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

while True:
    print("""welcome to BMI calculator:
    NOTE:
        -> height should be entered in meter
        -> weight should be in kg 
    guidlines: 
        if you don't know your height in meter or weight in kg then
        1. to convert height in meter
        2. to convert your weight in kg
        3. to convert both height and weight
        4. I already know my height in meter and weight in kg""")


    while True:
        user_choice = int(input("enter the option from above: "))
        if user_choice in (1,2,3,4):
            break
        else:
            print("enter the valid option from 1 to 4")
    if(user_choice == 1):
        height = height_conversion()
        weight = float(input("enter your weight in kg: "))
        BMI_calculator(height,weight)
    elif(user_choice == 2):
        height = float(input("enter your height in meter: "))
        weight = weight_conversion()
        BMI_calculator(height,weight)
    elif(user_choice == 3):
        height = height_conversion()
        weight = weight_conversion()
        BMI_calculator(height,weight)
    elif(user_choice == 4):
        weight = float(input("enter your weight in kg: "))
        height = float(input("enter your height in meter: "))
        BMI_calculator(height,weight)
    else:
        print("sorry for inconvinence")

    again = input("wanna calculate for other (yes/no): ").strip().lower()
    if(again != 'yes'):
        print("have a good day")
        break