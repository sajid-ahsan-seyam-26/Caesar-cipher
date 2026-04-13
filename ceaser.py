alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift_number = int(input("Type the shift number:\n"))


def encode_message(text, shift):
    final_text = ""

    for each_letter in text:
        if each_letter == " ":
            final_text = final_text + " "
        else:
            current_position = 0

            for letter in alphabet:
                if letter == each_letter:
                    new_position = current_position + shift

                    while new_position >= 26:
                        new_position = new_position - 26

                    final_text = final_text + alphabet[new_position]

                current_position = current_position + 1

    print("The encoded message is:", final_text)


def decode_message(text, shift):
    final_text = ""

    for each_letter in text:
        if each_letter == " ":
            final_text = final_text + " "
        else:
            current_position = 0

            for letter in alphabet:
                if letter == each_letter:
                    new_position = current_position - shift

                    while new_position < 0:
                        new_position = new_position + 26

                    final_text = final_text + alphabet[new_position]

                current_position = current_position + 1

    print("The decoded message is:", final_text)


if direction == "encode":
    encode_message(message, shift_number)
elif direction == "decode":
    decode_message(message, shift_number)
else:
    print("Invalid input")