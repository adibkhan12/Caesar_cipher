alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(encode_or_decode, original_text, shift_amount):
    if encode_or_decode == "encode":
        cypher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # third type of todo 4
            cypher_text += alphabet[shifted_position]
        print(f"Here is the encoded result:\n{cypher_text}")

    else:
        decrypted_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            decrypted_text += alphabet[shifted_position]
        print(decrypted_text)


ceasar(direction, text, shift)
