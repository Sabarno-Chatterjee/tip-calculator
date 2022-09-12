print("Welcome to the tip calculator\n")
raw_bill=input("What was the total bill? \n")

bill= float(raw_bill)

raw_tip=input("What percentage of tip would you like to give? 10, 12, or 15 \n")

tip= int(raw_tip)

raw_people=input("How many people to split the bill with?\n")

people=int(raw_people)

calc= float(bill*tip)
calc /= 100
calc = calc + bill
pay= calc/people
pay= round(pay, 2)



print(f"Each person should pay ${pay}.")