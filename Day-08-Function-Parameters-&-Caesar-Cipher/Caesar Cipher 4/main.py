alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    
    end_text = ""
    
    for letter in start_text:
      # Check if each character is alphabetic
        if letter.isalpha():
            # Position of letter in alphabet
            position = alphabet.index(letter)

            if cipher_direction == "encode":
                # Shift the letter by shift number
                new_position = (position + shift_amount) % 26            
            elif cipher_direction == "decode":
                # Shift the letter backwards by shift number   
                new_position = (position - shift_amount) % 26

            # Add the encrypted letter to cipher_text
            end_text += alphabet[new_position]
        else:
            # If letter is non-alphabetic, add it as it is
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

# Import and print the logo from art.py when the program starts.
import art
print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

run_cipher = True
while run_cipher:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            break

    text = input("Type your message:\n").lower()

    # Shift works for both +ve and -ve numbers
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except:
            pass

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        run_cipher = False
        print("Goodbye")