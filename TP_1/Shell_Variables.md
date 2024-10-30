## printing variables

running the command ``` echo $FLAG``` gave me the flag.($ was added because FLAG is a variable).

## setting variables

making a variable ```PWN=COLLEGE``` gave the flag.

## multi-worded variables

making a variable ```PWN="COLLEGE YEAH"``` gave the flag.

## exporting variables

i set ```PWN=COLLEGE``` and ```COLLEGE=PWN```. now, inorder to get the flag, i first had to export PWN ```export PWN``` and run ```/challenge/run``` to get the flag.

## printing exported variables

running ```env``` gave out the flag.(env prints out every exported variable in the shell environment)

![alt text](/assets/env.png "")

## storing command output

to practice command substitution, i first ran the command ```PWN=$(/challenge/run)``` ($before (challenge/run) since it is a variable) to set the value of PWN. after that, running ```echo $PWN``` gave me the flag.

## reading input

```read``` reads input from the user. running ```read PWN``` gave me the option to input the value of PWN, ie COLLEGE, which gave me the flag.

## reading files

to solve this chal, i redirected /challenge/read_me to PWN by running the command ```read PWN < /challenge/read_me``` which gave me the flag.

