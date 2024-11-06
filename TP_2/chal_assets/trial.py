lst = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

# print (len(lst))

# print(ord('a'))

import sys

def decrypt_mult(cipher, key):
    plaintext = []
    for c in cipher:
        plaintext.append(chr(int(c / (key * 311))))
    return ''.join(plaintext)

def decrypt_xor(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext

def main():
    cipher = [int(c) for c in sys.argv[1].split(',')]
    # Assuming the shared key is known or can be derived from the given information
    shared_key = lst # Replace with the actual shared key

    # Reverse multiplication encryption
    xor_cipher = decrypt_mult(cipher, shared_key)

    # Reverse dynamic XOR encryption
    plaintext = decrypt_xor(xor_cipher, "trudeau")

    print(plaintext)

if __name__ == "__main__":
    main()