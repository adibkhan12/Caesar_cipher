alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#my code in comment and the easier version is actual code.
letter=[]
#def encrypt(original_text, shift):
#     shifted_element = []
#     for letters in text:
#         letter.append(letters)
#     for x in letter:
#         index_of_x = alphabet.index(x)
#         shifts = alphabet[index_of_x+shift]
#         shifted_element.append(shifts)
#     original_text = "".join(shifted_element)
#     print(f"Here is the encoded result:\n{original_text}")
def encrypt(original_text, shift_amount):
    cypher_text=""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) # third type of todo 4
        cypher_text += alphabet[shifted_position]
    print(f"Here is the encoded result:\n{cypher_text}")
encrypt (text, shift)
