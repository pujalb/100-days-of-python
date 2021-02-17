# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_score = 0
love_score = 0

# Count the no of times the characters in "TRUE" occur in the 2 names 
for char in "true":
    true_score += (name1.lower()).count(char)
    true_score += (name2.lower()).count(char)
# Count the no of times the characters in "LOVE" occur in the 2 names
for char in "love":
    love_score += (name1.lower()).count(char)
    love_score += (name2.lower()).count(char)

# Combine the 2 scores to make a 2 digit number
final_score = f"{true_score}{love_score}"
final_score_int = int(final_score)

if (final_score_int < 10) or (final_score_int > 90):
    print(f"Your score is {final_score_int}, you go together like coke and mentos.")
elif 40 < final_score_int < 50:
    print(f"Your score is {final_score_int}, you are alright together.")
else:
    print(f"Your score is {final_score_int}.")


# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))