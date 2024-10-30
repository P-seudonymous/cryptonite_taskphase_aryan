## chaining with semicolons

to get the flag, i had to run the command ```/challenge/pwn; /challenge/college```

## your first shell script

this chal was straighforward, my procedure is in the image below.
![alt text](/assets/shell_scripting.png "")

## redirecting script output

i created a shell script(x,sh) with the necessary commands, and then piped it to ```challenge/solve``` to get the flag. following is the code block.

![alt text](/assets/piping_script.png "")

## executable shell scripts

i made a shell script, named ```script.sh```, and then wrote ```/challenge/solve``` to it. to make it executable, i used ```chmod u+x script.sh```. running ```./script.sh``` gave me the flag.

![alt text](/assets/executable.png)
