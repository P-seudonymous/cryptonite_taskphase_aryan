## changing file ownership

to get the flag, we had to use the command ```chown [username] [file]``` -> ```chown hacker /flag``` to change the ownership of flag to hacker.

after running ```cat /not-the-flag```, i got the flag.

![alt text](/assets/chown.png "")

## groups and files

to get the flag, i had to change the group of file to ```hacker``` user. this was accomplished by running ```chgrp hacker /flag```. running ```cat /not-the-flag`` gave me the flag.

## fun with group names

running id gave me info regarding the user ```hacker``` => ```uid=1000(hacker) gid=1000(grp16185) groups=1000(grp16185)```.

i ran the command ```chgrp grp16185 /flag``` to change the group of the file. running ```/flag``` gave me the flag.

##  changing permissions

i used the command ```chmod o+r /flag``` to give read permissions to all other users. after that, running ```cat /flag``` gave me the flag.

## executable files

to make the executable file, i ran ```chmod u+x /challenge/run```. after that, running ```/challenge/run``` gave me the flag.

## permission tweaking practice

this was a lenghty chal, purely testing if you know how to set permissions.

here is the terminal log.
```
hacker@permissions~permission-tweaking-practice:~$ /challenge/run
Round 0 (of 8)!

Current permissions of "/challenge/pwn": rw-r--r--
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": rwxr--r-x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod uo+x /challenge/pwn
You set the correct permissions!
Round 1 (of 8)!

Current permissions of "/challenge/pwn": rwxr--r-x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": rwx---r-x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod g-r /challenge/pwn
You set the correct permissions!
Round 2 (of 8)!

Current permissions of "/challenge/pwn": rwx---r-x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": rwx-----x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod o-r /challenge/pwn
You set the correct permissions!
Round 3 (of 8)!

Current permissions of "/challenge/pwn": rwx-----x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": rwxrwx--x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod g+rwx /challenge/pwn
You set the correct permissions!
Round 4 (of 8)!

Current permissions of "/challenge/pwn": rwxrwx--x
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": ---rwx--x
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod u-rwx /challenge/pwn
You set the correct permissions!
Round 5 (of 8)!

Current permissions of "/challenge/pwn": ---rwx--x
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": r-xrwxr-x
* the user does have read permissions
- the user doesn't have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod uo+rx /challenge/pwn
You set the correct permissions!
Round 6 (of 8)!

Current permissions of "/challenge/pwn": r-xrwxr-x
* the user does have read permissions
- the user doesn't have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
* the world does have read permissions
- the world doesn't have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": rwxrwxrwx
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
* the world does have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permission-tweaking-practice:~$ chmod uo+w /challenge/pwn
You set the correct permissions!
Round 7 (of 8)!

Current permissions of "/challenge/pwn": rwxrwxrwx
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
* the group does have write permissions
* the group does have execute permissions
```

finally to get the flag, i ran ```chmod u+r /flag``` and ```cat /flag``` gave me the flag.

## permissions setting practices

this chal was similar to the last one.
here is the procedure i followed to get the flag.

```hacker@permissions~permissions-setting-practice:~$ chmod u=rw,g=r,o=- /challenge/pwn
NEEDED, BUT UNMET permissions of "/challenge/pwn": ----w--w-
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

CURRENT, INCORRECT permissions of "/challenge/pwn": rw-r-----
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions

You set the permissions incorrectly! Restarting the game!
hacker@permissions~permissions-setting-practice:~$ chmod u=-,g=w,o=w /challenge/pwn
You set the correct permissions!
Round 1 (of 8)!

Current permissions of "/challenge/pwn": ----w--w-
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": rwx----wx
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=rwx,g=-,o=wx /challenge/pwn
You set the correct permissions!
Round 2 (of 8)!

Current permissions of "/challenge/pwn": rwx----wx
* the user does have read permissions
* the user does have write permissions
* the user does have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": rw--wx-w-
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=rw,g=wx,o=w /challenge/pwn
You set the correct permissions!
Round 3 (of 8)!

Current permissions of "/challenge/pwn": rw--wx-w-
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
* the group does have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": -wxr-x-wx
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=wx,g=rx,o=wx /challenge/pwn
You set the correct permissions!
Round 4 (of 8)!

Current permissions of "/challenge/pwn": -wxr-x-wx
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
* the world does have execute permissions

Needed permissions of "/challenge/pwn": ---r-x-w-
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=-,g=rx,o=w /challenge/pwn
You set the correct permissions!
Round 5 (of 8)!

Current permissions of "/challenge/pwn": ---r-x-w-
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": rw-r-xrw-
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=rw,g=rx,o=rw /challenge/pwn
You set the correct permissions!
Round 6 (of 8)!

Current permissions of "/challenge/pwn": rw-r-xrw-
* the user does have read permissions
* the user does have write permissions
- the user doesn't have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
* the world does have read permissions
* the world does have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": r----x---
* the user does have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=r,g=x,o=- /challenge/pwn
You set the correct permissions!
Round 7 (of 8)!

Current permissions of "/challenge/pwn": r----x---
* the user does have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions

Needed permissions of "/challenge/pwn": -wxr-x-w-
- the user doesn't have read permissions
* the user does have write permissions
* the user does have execute permissions
* the group does have read permissions
- the group doesn't have write permissions
* the group does have execute permissions
- the world doesn't have read permissions
* the world does have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod u=wx,g=rx,o=w /challenge/pwn
You set the correct permissions!
You've solved all 8 rounds! I have changed the ownership
of the /flag file so that you can 'chmod' it. You won't be able to read
it until you make it readable with chmod!

Current permissions of "/flag": ---------
- the user doesn't have read permissions
- the user doesn't have write permissions
- the user doesn't have execute permissions
- the group doesn't have read permissions
- the group doesn't have write permissions
- the group doesn't have execute permissions
- the world doesn't have read permissions
- the world doesn't have write permissions
- the world doesn't have execute permissions
hacker@permissions~permissions-setting-practice:~$ chmod o+r /flag
hacker@permissions~permissions-setting-practice:~$ cat /flag
cat: /flag: Permission denied
hacker@permissions~permissions-setting-practice:~$ chmod u+r /flag
hacker@permissions~permissions-setting-practice:~$ cat /flag
pwn.college{YjBn6SsooHvg-X8Nf8jSCZLctbA.dNTM5QDL0MDM2czW}
```

## the SUID bit

i used the command ```chmod u+s /challenge/getroot```. since i have set the user id, i can now run ```/challenge/getroot``` to become root. from there, running cat /flag gave me the flag.



