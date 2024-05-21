alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(start_text, shift_amount, ciper_direction):

    end_text = ""

    if ciper_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        index = alphabet.index(letter)
        new_position  = index+shift_amount

        if new_position > 25:
            new_position = new_position-26
        elif new_position < 0:
            new_position = new_position+26

        new_letter = alphabet[new_position]
        end_text += new_letter

    print(f"The {ciper_direction}d text is: {end_text}")

ceasar(text, shift, direction)



# def encrypt(plain_text, shift_place):
#     cipher_text = ""
#     for letter in plain_text:
#         index =  alphabet.index(letter)
#         new_position = index+shift_place

#         if new_position > 25:
#             new_position = new_position-26

#         new_letter =  alphabet[new_position]
#         cipher_text += new_letter

#     return cipher_text

# def decrypt(cipher_text, shift_place):
#     original_text = ""
#     for letter in cipher_text:
#         index = alphabet.index(letter)
#         new_position = index-shift_place
    
#         if new_position < 0:
#             new_position = new_position + 26

#         new_letter = alphabet[new_position]
#         original_text += new_letter

#     return original_text

# if direction == "encode":
#     cipher_text = encrypt(text, shift)
#     print(f"The encoded text is: {cipher_text}")
# elif direction == "decode":
#     original_text = decrypt(text, shift)
#     print(f"The decode text is: {original_text}")