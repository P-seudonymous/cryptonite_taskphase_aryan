## Tet-riffic

Flag: ``` ```

In this challenge, we were initially provided a .pcapng file, and a python file(tetris pygame). I got a little confused at first, but after fiddling around with the game and the .pcapng file, i realized that .pcapng file contained USB interrupts, and it was related to a keyboard(plugging in and out)

So I looked for the first character that contained HID data(the information sent by keyboard when a key is pressed).

I filtered out the HID data(which was in hex) using python and gave it as a stdout to a text file.
The hex data contained over 6k lines, i'll attach it here.

[text](assets/hexd.txt)

Then using python(i did not write the script, got it off the internet), converted HID -> string and got an output as ``` w a w a space``` etc.
[text](assets/script.py)

[text](assets/flag.txt) 

[text](assets/output.txt)



