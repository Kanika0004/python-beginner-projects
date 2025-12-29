print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_perc=int(input("How much tip would you like to give? 10, 12, or 15"))
no_people=int(input("How many people to split the bill?"))
per_person_bill=(total_bill+(total_bill*(tip_perc/100)))/no_people
print(f"Each person should pay: ${per_person_bill}")

































# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15? "))
# people = int(input("How many people to split the bill? "))
# T_tip= tip * bill / 100
# T_tamt= (bill + T_tip)
# T_amt= T_tamt/people
# amt=round(T_amt,2)
# print(f"Each person should pay : ${amt:.2f}")



