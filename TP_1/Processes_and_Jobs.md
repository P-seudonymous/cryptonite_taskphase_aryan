## listing processes

to get the flag, i ran ```ps aux``` which gave me the running processes, from there i found the program/command ```/challenge/9587-run-20687```, running which, gave me the flag.

## killing processes

again, by running ```ps aux``` i got the PID  of ```/challenge/dont-run``` which was 73.
running ```kill 73``` killed the process. after that, i executed ```/challenge/run``` which gave me the flag.

## interrupting processes

running ```ctrl+c``` gave me the flag.

## suspending processes

running ```ctrl+z``` suspends processes, using that command twice gave me the flag.

## resuming processes

in this chal, i had to execute ```ctrl+z``` and then run ```fg```, which resumes the process and puts it back in the foreground.

## backgrounding processes

in this chal, i had to run ```/challenge/run``, suspend it using ```ctrl+z``` and then background it using ```bg```, after which i had to run ```/challenge/run`` again to get the flag.

## foregrounding processes

this chal was straightforward. the file attached below shows how i got the flag.

![alt text](/assets/foregrounding.png)

## starting backgrounded processes

appending ```&``` after a program, makes the process start backgrounded. similarly, running the command ```/challenge/run &``` gave me the flag.

## process exit codes

this chal was also pretty simple, the key command here was ```echo $?``` which tells the error code if a program exits/fails to run.

the following codeblock shows how i got the flag.

![alt text](/assets/error.png)