print("welcome to tip calculator\n")

def main():
    while True:
        while True:
            try:
                total_bill = float(input("total bill amount: "))
                tip_percent = float(input("what amount you want to give as tip(in percent): "))
                people = int(input("the number of people gonna contribute: "))
                if (tip_percent >= 0) and (total_bill >= 0) and (people >= 1):
                    tip = ((tip_percent/100)*total_bill)
                    print(f"the amount to be given as tip: {tip}")
                    print("the total bill to be paid: ", total_bill+tip)
                    print("bill per person: ", (total_bill+tip)/people)
                    break
                else:
                    print("invalid data please reconsider your data")
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
        
        again = input("wanna calculate another bill(yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("have a good day")
            break

if __name__ == "__main__":
    main()
            