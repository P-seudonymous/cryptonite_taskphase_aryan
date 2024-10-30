## matching with *

to change the directory, i ran the command ```cd /ch*``` which changed the directory to challenge.
from there, running ```/challenge/run``` gave me the flag.

## matching with ? 
to change the dir, i executed ```cd /?ha??enge``` which changed the directory to challenge.
running ```/challenge/run``` gave me the flag.

## matching with []

first, we had to change the dir to /challenge/files. after that, running ```/challenge/run file_[bash]``` gave me the flag.

## matching paths with []

since we had to pass a single line command, i ran ```/challenge/run /challenge/files/file_[bash]``` which gave me the flag.

## mixing globs

first, i changed the dir to ```/challenge/files```, now since the argument has to be 6 chars or less, i ran 
```/challenge/run [pce]*``` which gave me the flag, pce being the initial chars of all the files.

## exclusionary globbing

i changed the dir to ```/challenge/files```, now to get the flag, i ran ``` /challenge/run [!pwn]*``` which gave me the flag.