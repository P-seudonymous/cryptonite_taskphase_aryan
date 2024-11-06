## GDB baby step 1

Flag: ```picoCTF{549698}```

Hints used: NONE

this chal required knowledge related to the gnu debugger, aka, gdb. 

to get the flag, i first downloaded the file [debugger0_a](/TP_2/chal_assets/debugger0_a). The file was not executable, so i made it executable by running ```chmod u+x debugger0_a```.

then i ran ```gdb ./debugger0_a``` in terminal. after that, i ran ```lay next```, which gave me the source code(in ASM) of the file.

after looking around, i found the a line with ```%eax```, which should presumable be the eax register. (However, running print $eax returned no registers.)

the following image is where i found the flag.

![ALT TEXT](/assets/gdb_tp2.png)

## ARMssembly 1

Flag: ```picoCTF{00000715}```

Hints used: Shift register

in this challenge, i was given an ```.asm``` file, where there were 3 variables, ```85, 6, 3```. 85 was being stored in ```w0``` and it was being Left shifted by 6 bits. [LINE 18]
```Left shift is done by converted the decimal(here 85) into a binary number, and then appending n(here 6) 0s at the end.```
```85 => 1010101; now, 1010101 << 6 => 1010101000000. this number corresponds to 5440(base 10).```
after that, 5440 is being divided by 3, which gives 1813(int div) [LINE 22]

around the end of ```func```, it subtracts w0(original argument) from 1813. To get the flag(you win!), ```w0 - 1813 ==0``` i.e. input should be equal to 1813. [LINE 26]

converting 1813 to hex gave me 715, and since the int should be 8 bit, the argument for the flag was ```00000715```.

asm file: [chall_1.S](/TP_2/chal_assets/chall_1.STP2)

Wrong Tangents: Wasted more than an hour trying to find the right tools, packages and compilers to run the asm file, in which i failed miserably, since i kept getting random errors while compiling the file.
after that, i realized that maybe reading the asm file could solve the chal, which was what eventually worked.

## 