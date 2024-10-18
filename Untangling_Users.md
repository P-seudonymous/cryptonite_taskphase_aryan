## becoming root with su

running ```su``` gave me the option to input password and change user to root. after entering the password, i got root perms. after running ```ls -l``` i saw a file ```not-the-flag -> flag``` which must have been an old symbolic link which i created. running ```cat not-the-flag``` gave me the flag

here is the code log
```
hacker@users~becoming-root-with-su:~$ su
Password: 
root@users~becoming-root-with-su:/home/hacker# /challenge/run
In the previous level, you used the `/challenge/getroot` program to become the `root` user.
Becoming root is a fairly common action that Linux users take, and your typical Linux installation obviously does not have `/challenge/getroot`.
Instead, there are two utilities used for this purposes: `su` and `sudo`.

In this challenge, we will cover the older one, `su` (the **s**witch **u**ser command).
This is not typically used to elevate to root access anymore, but it is an elegant utility from a more civilized time, and we'll cover it first.

`su` is a setuid binary:

```console
hacker@dojo:~$ ls -l /usr/bin/su
-rwsr-xr-x 1 root root 232416 Dec 1 11:45 /usr/bin/su
hacker@dojo:~$
```

Because it has the SUID bit set, `su` runs as root.
Running as root, it can start a root shell!
Of course, `su` is discerning: before allowing the user to elevate privileges to root, it checks to make sure that the user knows the root password:

```console
hacker@dojo:~$ su
Password: 
su: Authentication failure
hacker@dojo:~$
```

This check against the root password is what obsoletes `su`.
Modern systems very rarely have root passwords, and different mechanisms (that we will learn later) are used to grant administrative access.

But THIS challenge (and only this challenge) _does_ have a root password.
That password is `hack-the-planet`, and you must provide it to `su` to become root!
Go do that, and read the flag!
root@users~becoming-root-with-su:/home/hacker# /flag
bash: /flag: Permission denied
root@users~becoming-root-with-su:/home/hacker# ls -l
total 20
drwxr-xr-x 3 hacker hacker 4096 Oct  8 20:28 Desktop
-rw-r--r-- 1 root   hacker   58 Oct  8 20:36 a
-rw-r--r-- 1 hacker hacker    0 Oct 15 15:58 college
-rw-r--r-- 1 hacker hacker    0 Oct  8 20:26 file.txt
drwxr-xr-x 2 hacker hacker 4096 Oct  8 20:36 h
-rw-r--r-- 1 hacker hacker    0 Oct  8 20:27 h.txt
drwxr-xr-x 2 hacker hacker 4096 Oct  8 20:33 hi
-rw-r--r-- 1 hacker hacker    0 Oct  8 20:26 hi.txt
drwxr-xr-x 2 hacker hacker 4096 Oct  8 20:23 lol
lrwxrwxrwx 1 hacker hacker    5 Oct 15 16:12 not-the-flag -> /flag
root@users~becoming-root-with-su:/home/hacker# ./flag
bash: ./flag: No such file or directory
root@users~becoming-root-with-su:/home/hacker# /not-the-flag
bash: /not-the-flag: No such file or directory
root@users~becoming-root-with-su:/home/hacker# cat not-the-flag
pwn.college{s8wh_xi-5vW2h-XLn6paXxnvXyJ.dVTN0UDL0MDM2czW}```

## other users with su

this chal was straightforward, all i had to do was switch to zardus by running ```su zardus``` and after giving the password, i had to run ```/challenge/run``` which gave me the flag.

## cracking passwords

in this chal, we used a hashing package(john the ripper) to crack zardus's password.
by running the command ```john /challenge/shadow-leak``` i got the password for zardus.

![alt text](/assets/hashing.png "")

after su to zardus, and running ```/challenge/run``, i got the flag. 

## using sudo

this chal was very simple. following is the procedure i followed to get the flag.

![alt text](/assets/sudo.png "")
