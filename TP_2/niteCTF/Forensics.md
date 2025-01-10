## Tet-riffic

Flag: ``` ```

In this challenge, we were initially provided a .pcapng file, and a python file(tetris pygame). I got a little confused at first, but after fiddling around with the game and the .pcapng file, i realized that .pcapng file contained USB interrupts, and it was related to a keyboard(plugging in and out)

So I looked for the first character that contained HID data(the information sent by keyboard when a key is pressed).

I filtered out the HID data(which was in hex) using python and gave it as a stdout to a text file.
The [hex data](assets/hexd.txt) contained over 6k lines.

head:

```
020000130000000000
020000000000000000
0200001c0000000000
020000000000000000
020000170000000000
020000000000000000
0200000b0000000000
020000000000000000
020000120000000000
020000000000000000
```


Then using python(i did not write the script, got it off the internet), converted HID -> string and got an output as ``` w a w a space``` etc.
[script](assets/script.py)

This was the [output](assets/flag.txt) from the script, which i converted to a [single string](assets/output.txt).



