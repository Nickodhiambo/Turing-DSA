#!/usr/bin/env python

"""
Takes an encoded Cypher text and a plain text. The plain text is a fragment of the decoded string. Use the fragment to
decode the entire string, preserving special characters and
case
"""

# Plan
# We know every letter of the cypher text has been shifted 
# forward by a consistent key. We first need to determine
# this shift
# Use the shift to decode every letter of the cypher
# Return the decoded string

def decode_cypher_text(cypherText: str, key: int) -> str:
    """
    Helper function that takes key and decodes cypher
    """
    if key == 0:
        return cypherText
    decoded_str = []
    
    # Loop through every char of cyphertext, shifting it back
    for char in cypherText:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded = chr((ord(char)- base - key) % 26 + base)
            decoded_str.append(decoded)
        else:
            decoded_str.append(char)
    return ''.join(decoded_str)

def decoder(cypherText: str, plainText: str) -> str:
    # We need to infer which encrypted word is plain text
    # They have to be of exactly the same length,
    # and every letter of the encrypted word should have
    # been shifted by a consistent key

    keys = []
    key = 0

    words = cypherText.split(' ')
    for word in words:
        if len(word) != len(plainText):
            continue
        else:
            # We are checking if key is consistent for
            # every letter of the current word
            for char1, char2 in zip(word, plainText):
                shift = (ord(char1) - ord(char2)) % 26
                keys.append(shift)
            if len(set(keys)) == 1:
                key += keys[0]
                break
    print(key)

    # Now use key to decode string
    decoded_str = decode_cypher_text(cypherText, key)
    return decoded_str

if __name__ == '__main__':
    print(decoder('Khoor Zruog', 'Hello'))
    print(decoder('Zxbpxo qbuq', 'Caesar'))
    print(decoder('Mjqqt Btwqi', 'Hello'))
    print(decoder('Khoor, Zruog!', 'World'))
    print(decoder('Khoor Zruog', 'Python'))

