import art
print(art.logo)  # Displaying a logo from the art module

# Alphabet list used for encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to handle both encryption and decryption
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If decoding, the shift is reversed (negative shift)
    if encode_or_decode == "decode":
        shift_amount *= -1
        for letter in original_text:
            if letter in alphabet:
                # Find the new shifted position with wrapping using modulo
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter  # Leave non-alphabet characters unchanged
    
    # If encoding, the shift remains positive
    if encode_or_decode == "encode":
        shift_amount *= 1
        for letter in original_text:
            if letter in alphabet:
                # Find the new shifted position with wrapping using modulo
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter  # Leave non-alphabet characters unchanged
    
    # Print the result (encrypted or decrypted)
    print(f"Here is the {encode_or_decode}d result: {output_text}")


game_over = False
# Game loop to allow repeated encoding/decoding
while not game_over:
    # Get user inputs for direction, text, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar cipher function with user inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to run the program again
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        game_over = True
        print("Goodbye")
