## redirecting output

in this chal, i had to redirect stdout(```PWN```) to file ```COLLEGE``` by running the command ```echo PWN > COLLEGE``` which gave me the flag.

## redirecting more output

in this chal, i had to redirect stdout ```/challenge/run``` to ```myflag```.
running the command ```/challenge/run > myflag``` satisfies this condition. running ```cat myflag``` gave me the flag.

## appending output

here, append mode (```>>```) was to be used to append text at the end of the file(like appending elements into a list in python.)

the following code block is my procedure of getting the flag.
```
hacker@processes~backgrounding-processes:~$ /challenge/run
I'll only give you the flag if there's already another copy of me running *and 
not suspended* in this terminal... Let's check!

UID          PID STAT CMD
Connected!                                                                        
hacker@piping~appending-output:~$ /challenge/run >> /home/hacker/the-flag
[INFO] WELCOME! This challenge makes the following asks of you:
[INFO] - the challenge will check that output is redirected to a specific file path : /home/hacker/the-flag

[HYPE] ONWARDS TO GREATNESS!

[INFO] This challenge will perform a bunch of checks.
[INFO] Good luck!

[TEST] You should have redirected my stdout to a file called /home/hacker/the-flag. Checking...

[HINT] File descriptors are inherited from the parent, unless the FD_CLOEXEC is set by the parent on the file descriptor.
[HINT] For security reasons, some programs, such as python, do this by default in certain cases. Be careful if you are
[HINT] creating and trying to pass in FDs in python.

[PASS] The file at the other end of my stdout looks okay!
[PASS] Success! You have satisfied all execution requirements.
I will write the flag in two parts to the file /home/hacker/the-flag! I'll do 
the first write directly to the file, and the second write, I'll do to stdout 
(if it's pointing at the file). If you redirect the output in append mode, the 
second write will append to (rather than overwrite) the first write, and you'll 
get the whole flag!
hacker@piping~appending-output:~$ cat /home/hacker/the-flag
 | 
\|/ This is the first half:
 v 
pwn.college{EViyFuVXBGrQlxeOxWIDjCVM8Gq.ddDM5QDL0MDM2czW}
                              ^
     that is the second half /|\
                              |

If you only see the second half above, you redirected in *truncate* mode (>) 
rather than *append* mode (>>), and so the write of the second half to stdout 
overwrote the initial write of the first half directly to the file. Try append 
mode!
```

## redirecting errors

important info for this chal => 
```
FD 0: Standard Input => <
FD 1: Standard Output => >
FD 2: Standard Error => 2>
```

the file below shows the procedure to get the flag.
![alt text](/assets/stderr.png)

## redirecting input

this was pretty straightforward, the file shows how i got the flag.
![alt text](/assets/stdin.png)

## grepping stored results

in this chal, i had to redirect ```/challenge/run``` to ```/tmp/data.txt``` and then search for the flag using the command ```grep pwn.college /tmp/data.txt```.

## grepping live output

here, the concept of 'piping' ie connecting 2 files was used.
```stdout``` is piped into ```stdin``` of the command.

the file below shows my procedue.
![alt text](/assets/piping.png)

## grepping errors

```>&``` operator redirects a file descriptor to another file descriptor.

to get the flag, i ran the command ```/challenge/run 2>&1 | grep pwn.college``` where ```2>&1``` stands for redirecting ```stderr``` to ```stdout```.

## duplicating piped data with tee

```tee``` reads the standard input and writes it to both the standard output and one or more files. named after the T-splitter in plumbing.

```/challenge/pwn | tee x | /challenge/college```, where tee reads the stdin to x.

the following file shows how i got the flag.
![alt text](/assets/tee.png)

## writing to multiple programs

in this chal, i needed to pipe the output of ```/challenge/hack``` into both ```/challenge/the``` and ```/challenge/planet```.

``` tee >(commands)``` is the syntax for commands.

i ran the command ```/challenge/hack | tee >(/challenge/the) | /challenge/planet``` which gave me the flag.

## split-piping stderr and stdout

this chal was similar to the last one.
the following code shows how i got the flag.
![alt text](/assets/split_piping.png)