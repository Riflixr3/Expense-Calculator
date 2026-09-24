import sys

def calculate(total, people, tip):

    if tip > 0:
        tip_amount = total * (tip / 100)
        total_with_tip = total + tip_amount
        pay = round(total_with_tip / people, 2)


        print("Bill:",total)
        print("Tip: ",tip_amount)
        print("Total: ",total_with_tip)
        print("Per person: ",pay)

    else:
        pay = round(total / people, 2)

        print("Bill:",total)
        print("Tip: 0")
        print("Total: ",total)
        print("Per person: ",pay)


total = float(input("Enter the total bill: "))

if total <= 0:
    print("Invalid bill")
    sys.exit()
    
        

people = int(input("Enter the total number of people: "))

if people <= 0:
        print("People can't be ", people)
        sys.exit()

 
tip = float(input("How much % tip is: "))

if tip <= 0:
    tip = 0 

calculate(total, people,tip)

