# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# no of names given as input
count = len(names)

#Choose a random int within count
random_num = random.randint(0, count - 1)

chosen_one = names[random_num]
print(f"{chosen_one} is going to buy the meal today!")


