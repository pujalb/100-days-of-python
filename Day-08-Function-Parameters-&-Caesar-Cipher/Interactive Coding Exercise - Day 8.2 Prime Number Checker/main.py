#Write your code below this line 👇
from math import sqrt, ceil
def prime_checker(number):

    # Ceck if number is greater than 1
    if number < 2:
        print("It's not a prime number.")
        return

    # Instead of checking all numbers from 0 to number, just check from 0 to square root of the number
    last_num = ceil(sqrt(number))

    is_prime = True
    for num in range(2, last_num):
        if number % num == 0:
            is_prime = False
    
    if is_prime:
        print("It's a prime number.") 
    else:
        print("It's not a prime number.") 

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



