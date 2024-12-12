##  C3

Flag: ```picoCTF{adlibs}```

Hints Used: NONE

In the chal, i was given a .txt file and a python script, which was not yielding any output.

while fiddling around with the script, i added a new variable(var) and added its value to ```out``` & assigned the value of ```lookup1.index(var)``` to ```prev```.

Here is the edited script.

```
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup2.index(char)
  var = lookup1[(cur + prev) % 40]
  out += lookup1[(cur + prev) % 40]
  prev += lookup1.index(var)

sys.stdout.write(out)
```

Here is the output code.

```
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

now, runnning ```python convert.py ciphertext``` gave me another code, in python 2, which after after adding () to the ```print``` function worked normally.
since it is a self input code, i ran ```python decoder.py decoder.py``` and got the output as 
```
a
d
l
i
b
n
```
which is not the answer.

so i edited the code and got
```
a
d
l
i
b
s
```

here is the edited code, i edited the ```b``` variable in both the main code and loop, and changed the range to ```(0,len(chars))```

```
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1

for i in range(0,len(chars)):
    if i == b * b * b:
        print (chars[i]) #prints
        b += 1
```

## Custom Encryption

Flag: ```picoCTF{custom_d2cr0pt6d_019c831c}```

Hints Used: NONE

This challenge seemed very tricky at first, but when i traversed through the code, i realised that around 3-4 functions needed to be made to reverse the cipher, and i had to write the code for checking if the key was correct or not, so that the cipher can be decoded correctly.

I wrote the following fucntions:

``` decrypt(cipher, key)```, line 14
in this func, i just reversed the process of encrypt function.

```dyn_xor_decrypt(plaintext, text_key)```, line 42
to reverse an XOR encrytion, the cipher needs to be XOR-ed again with the same key, so added the loop in the same function, but that did not give me the correct flag, so i looped it 3 times inside the function(hit and trial method) and that gave me the flag.

now, since i already had values for ```a``` and ```b```, i copied the ```test()``` function, and wrote it once again, and compared the key with ```b_key```, added the cipher from the file and used the ```dyn_xor_decrypt(plaintext, text_key)``` function with ```semi_cipher``` as plaintext and ```trudeau``` as key.

Here is the code attached. ![custom decryption](/TP_2/chal_assets/custom_decryption.py)

```
from random import randint
import sys


def generator(g,x,p):
    return pow(g, x)%p

def encrypt(plaintext, key):
    cipher =[]
    for char in plaintext:
        cipher.append(((ord(char)*key*311)))
    return cipher

def decrypt(cipher, key):
    plaintext = ""
    for encrypted_value in cipher:
        decrypted_value = encrypted_value // (key*311)
        plaintext += chr(decrypted_value)
    return plaintext    


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def dyn_xor(plaintext, text_key):
    cipher_text=''
    key_length = len(text_key)

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))

        cipher_text+=encrypted_char
    return cipher_text
def dyn_xor_decrypt(plaintext, text_key):
    cipher_text=''
    key_length = len(text_key)

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))

        cipher_text+=encrypted_char

    plaintext = cipher_text
    cipher_text=''
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))

        cipher_text+=encrypted_char
        plaintext = cipher_text
 
    cipher_text = ""

    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text



def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dyn_xor(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


p =97
g = 31
a = 88
b = 26

u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)

shared_key = None
if key == b_key:
    shared_key = key
else:
    print("invalid key")


cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]
semi_cipher = decrypt(cipher, shared_key)
flag = dyn_xor_decrypt(semi_cipher, "trudeau")

print(flag)



# if __name__ == "__main__":
#     # message = sys.argv[1]
#     # test(message, "trudeau")

```







