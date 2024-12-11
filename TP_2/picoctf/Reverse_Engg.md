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

## VaultDoor3

Flag: ```picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}```

Hints Used: NONE

In the following challenge, we had a .java file in which input, after going through 4 for loops is being compared with a string.

also, in the java file, scanner was not closed, so i added the ```scanner.close()``` line at the end of the main func.

since the flag is supposed to be the same string, but jumbled(since loops are begin implemented).
so, to get the flag, i wrote a simple python script that takes the string as input, and implements for_loops in reverse order, like 1->4, 2->3. 3->2 and so on.

from that, i got the the correct string, and adding picoCTF{} to it gave me the flag.

Here is the code given in the challenge.

```
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();

	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);

	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
        scanner.close(); // added this line manually to the code.

    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}
```


Here is the script i wrote.![python script](/cryptonite_taskphase_aryan/TP_2/chal_assets/VaultDoor3.py)
```
str = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'
buffer = [''] * 32

for i in range(31,16,-2):
    buffer[i] = str[i]

for i in range(16, 32, 2):
    buffer[i] = str[46 - i]
    
for i in range(8, 16):
    buffer[i] = str[23-i]

for i in range(8):
    buffer[i] = str[i]


print(''.join(buffer))

```
