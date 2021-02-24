alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
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

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text = text, shift_amount = shift, cipher_direction = direction)