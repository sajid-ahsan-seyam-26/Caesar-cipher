# Caesar-cipher
# Caesar-cipher
# Beginner Friendly Caesar Cipher in Python

This is a beginner-friendly Python project.

It can:

- encode a message
- decode a message

This project uses the Caesar Cipher method.

---

## What is Caesar Cipher?

Caesar Cipher is a simple encryption method.

It works by shifting each letter by a fixed number.

Example:

- `a` with shift `2` becomes `c`
- `b` with shift `2` becomes `d`
- `z` with shift `2` becomes `b`

So letters move forward or backward in the alphabet.

---

## Features

- Encode text
- Decode text
- Keeps spaces unchanged
- Easy to understand
- Good for Python beginners

---

## How the program works

The program asks the user for 3 things:

1. `encode` or `decode`
2. the message
3. the shift number

Then it processes each letter and shows the final result.

---

## Code

```python
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
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
The encoded message is: khoor zruog
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
The decoded message is: hello world
Concepts used in this project

This project helps beginners practice:

Python lists
functions
loops
if-else conditions
strings
user input
basic encryption logic
Why this project is good for beginners

This project is good for beginners because it is simple and teaches core Python ideas in one small project.

You can learn:

how to take input
how to use functions
how to work with letters
how to build logic step by step
Future improvements

You can improve this project by adding:

support for symbols
support for numbers
repeat option
better UI
one function for both encode and decode
