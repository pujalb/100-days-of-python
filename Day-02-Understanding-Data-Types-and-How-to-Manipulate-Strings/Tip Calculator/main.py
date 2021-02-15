#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Greeting
print("Welcome to the tip calculator!")

# convert bill to a float value
bill = float(input("What was the total bill? $"))

# convert tip to floating value
tip = float(input("How much tip would you like to give? 10, 12, or 15?" ))

# convert num_people to a int value
num_people = int(input("How many people to split the bill?"))

# Total bill
bill += bill * (tip / 100)

# Split the bill among the no of people
final_bill = (bill / num_people)

# Format the final bill to 2 decimal places
final_bill = round(final_bill, 2)

print(f"Each person should pay: ${final_bill}")