def calculate(total, people, tip):
    if tip > 0:
        tip_amount = total * (tip / 100)
        total_with_tip = total + tip_amount
        pay = round(total_with_tip / people, 2)

        print("Each person pays:", pay)

    else:
        pay = round(total / people, 2)

        print("Each person pays:", pay)


total = float(input("Enter the total bill: "))
people = int(input("Enter the total number of people: "))
tip = float(input("How much % tip is: "))

calculate(total, people, tip)