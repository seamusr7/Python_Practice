#tip calculator

print("welcome to the tip calculator")
total_bill = float(input("what was the total bill?\n"))
tip_amount = int(input("how much tip would you like to give? 10, 12, or 15?\n"))
num_people = int(input("how many people to split the bill?\n"))

tip_percentage = (tip_amount) / 100
split_pay = round(((total_bill * tip_percentage) + total_bill) / num_people, 2)

print(f"Each person should pay: {split_pay}")