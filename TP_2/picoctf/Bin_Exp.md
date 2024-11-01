## buffer overflow 0

Flag: ```picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}```
Hints used: NONE

in this chal, i gave a long string as an input ```11111111111111111111111111``` which gave me the flag. 
giving an input of ```111``` exited the program. however, when i inputted ```aaaaaaaaaaaaaaaaaaaaaaaaaaaa``` there 
was no output, and i had to press ```enter``` to exit the code.

after looking at the source code, there was a vulnerability for char greater than 16, however entering 17 chars didnt give me the flag, it took 20 chars to get the flag.
tried to understand the code but since i dont know c properly(skill issue), i cant really decode the script.

## format string 0

Flag: ```picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_ef312157}```
Hints used: NONE

the obvious choices were the ones with ```%``` in them, since they're used to format strings/output in C.
however after looking at the source_code, things made more sense.
in the first problem, input needs to have integers more than the buffer size set(32 bits)
```count > 2 * BUFSIZE```, since 1 int == 32 bits and ```Gr%114d_Cheese``` has 3 integers, that passes the value.
in the second problem, it is just looking for an integer formatting style, ie ```%s```, so ```Cla%sic_Che%s%steak``` gives me the flag.

qn for the mentor: why did the program return ```ClaCla%sic_Che%s%steakic_Che(null)``` in the end?

attaching the image for reference.

![alt text](/assets/format_tp2.png)

