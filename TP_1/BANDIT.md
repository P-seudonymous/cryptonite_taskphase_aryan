## lvl 1

```cat readme``` gave me the password.

## lvl 2

running ```cat -``` did not work as it acted as a command which redirected me to new line.
therefore, i cd'd into ```/``` and ran ```cat /home/bandit1/-``` and it gave me the password.

## lvl 3

since the filename had spaces, i ran ```cat spaces\ in\ this\ filename``` and it gave me the password.

## lvl 4

in this lvl, the file was hidden in the directory ```/inhere```. running ```ls -a``` showed me the file, and then catting it gave me the password.

## lvl 5

i couldn't find any optimal solution for this problem, so i opened 7 files manually until i found the password. -file07 contained the password.

## lvl 6
in this chal, to find the file, i ran the code ```find -size 1033c``` when i was inside ```/inhere```.
this gave me the location of the file, and catting it gave me the password.

## lvl 7

in this chal, running ```find / -type f -user bandit7 -group bandit6 -size 33c``` gave me a lot of errors(basically the log showed all files with :permission denied:)

so, i redirected all the files to ```/dev/null``` ie it deleted the data.

running ```find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null``` gave me the password.

## lvl 8

this chal was straightforward, i had to search for millionth in the ```data.txt``` file.
running ``` grep millionth data.txt``` gave me the password.

## lvl 9

since the line occurs only once, i used the command ```uniq -u``` in combination with ```sort```(i sorted the file since the password is the line that occurs only once in the file. ).

the following code gave me the password; ```sort data.txt | uniq -u```.

## lvl 10

since i want a human readable string, i used the ```strings``` command which distinguishes b/w human readable strings.

running ```strings data.txt | grep ==``` gave me the password.

## lvl 11

in this chal, we need to decode base64 encoded file. for that, we can use the builtin commands in linux.
```base64 -d``` can decode a base64 encoded file.

running the command ```base64 -d data.txt``` gave me the password.

## lvl 12

since we are rotating the chars by 13 alphabets, we are using ROT13 substitution.

in this chal, i can easily use any online decoder(https://dcode.fr/en), but to solve this in shell, we can use the ```tr``` command ie translate.

in order to substitute, i made an alias for rot13 => ```alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"``` and then ran ```cat data.txt | rot13``` which gave me the password.

## lvl 13

this chal was too complicated and hard, here are the important details needed to crack these types of chals.

hexdumps => ```xxd <inputFile> <outputFile>```
header file(gzip) => 1f8b08
header file(bzip2) => 425a68
header file(tar archive) => 646174

i had to compress/decompress a lot of files to get the password.

## lvl 14

the following command is used to transfer data over the internet, using ssh.
```scp -P <port> <user>@<IP>:<remotefilepath> <localfilepath>```












