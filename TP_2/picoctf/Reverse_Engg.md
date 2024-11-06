## GDB baby step 1

Flag: picoCTF{549698}

Hints used: NONE

this chal required knowledge related to the gnu debugger, aka, gdb. 

to get the flag, i first downloaded the file [debugger0_a](/chal_assets/debugger0_a). The file was not executable, so i made it executable by running ```chmod u+x debugger0_a```.

then i ran ```gdb ./debugger0_a``` in terminal. after that, i ran ```lay next```, which gave me the source code(in ASM) of the file.

after looking around, i found the a line with ```%eax```, which should presumable be the eax register. (However, running print $eax returned no registers.)

the following image is where i found the flag.

![ALT TEXT](/assets/gdb_tp2.png)

