print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many people to split the bill? "))
total_tip = total_bill * (percentage_tip /100)
bill_per_person = (total_bill + total_tip) / people_to_split
final_amt = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amt}")
