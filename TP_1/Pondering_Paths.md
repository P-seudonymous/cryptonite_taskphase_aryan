## The root

we need to run /pwn, which give the path of the root directory.

## Program and absolute path

we need to run /challenge/run, which give the flag.

## Position thy self

you need to change the directory to /usr/share/zoneinfo/posix/Asia, from where you need to execute /challenge/run.

## Position elsewhere

similar to the last challenge, you need to cd to /usr/share/build-essential, from where you need to run /challenge/run.

## Position yet elsewhere

again similar to the last challenge, you need to cd to /var , from where you need to run /challenge/run.

## implicit relative paths, from /

since the corrent working directory was / , the relative path was just challenge/run, without the / infront of challenge.

## explicit relative paths, from /

you needed to cd to /, the execute ./challenge/run, calling the dir by ., since a relative path was required.

## implicit relative path

inorder to launch run, ./run was to be executed, from /challenge dir. so the procedure was to cd into /challenge and then execute ./run.

## home sweet home

to get the flag, you need to run /challenge/run and the for the argument, which would be ~/a or any other character, which satisfies the 3 char condition.




