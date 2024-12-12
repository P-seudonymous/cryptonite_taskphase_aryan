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


