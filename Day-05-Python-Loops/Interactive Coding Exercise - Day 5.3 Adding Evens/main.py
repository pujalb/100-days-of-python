#Write your code below this row 👇

even_sum = 0

for number in range(1, 101):
    if (number % 2) == 0:
        even_sum += number

print(f"The sum of all the even numbers from 1 to 100 is {even_sum}")

# Alternate
even_sum = 0
for number in range(0, 101, 2):
   even_sum += number 
print(f"The sum of all the even numbers from 1 to 100 is {even_sum}")