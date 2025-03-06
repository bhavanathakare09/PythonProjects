# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, direction_process):
    if direction_process == "decode":
        shift_amount *= -1

    cipher_text = ""

    for letter in original_text:

        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the result: {cipher_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

set_cipher = True

while set_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction_process=direction)
    continue_job=input("Do you still want to continue type Yes or No\n").lower()
    if continue_job == "no":
        set_cipher = False
        print("Thank you, Goodbye")
    else:
        set_cipher = True






