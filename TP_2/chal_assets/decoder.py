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