## the PATH variable

this challenge was pretty straightforward. all i had to do was run ```PATH=""``` which would mess with the ```rm``` command. after that, i ran ```/challenge/run``` which gave me the flag.

## setting PATH

in this chal, i had to set ```PATH=/challenge/more_commands/```. after that, running ```/challenge/run``` gave me the flag.

## adding commands

i used the read command(since its builtin to bash)
the code in win was 
```
read -r flag < /flag
echo $flag
```
![alt text](/assets/PATH.png)

## hijacking teams

this chal was similar to the last one. the code in rm was ->
```
read flag < /flag
echo $flag
```
below is the procedure that i followed.
![alt text](/assets/hijack.png)

