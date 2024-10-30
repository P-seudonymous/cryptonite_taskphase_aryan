## cat, not the pet, but the command

cat command is used to read out files, in this challenge, we just had to execute "cat flag" to get the flag.

## catting absolute paths

to get the flag, i had to cd to the "/" directory, by running cd .. , i reached the path, from where, running cat /flag gave me the flag.

## more catting practice

the path to the flag was already given in the challenge, so i just had to run cat /usr/include/X11/flag

![alt text](/assets/catting.png "")

## grepping for a needle in a haystack

this challenge was straightforward, we had to use the grep command to search for the flag in /challenge/data.txt.

running the command "grep pwn.college /challenge/data.txt" gave me the flag.

## listing files

for the following challenge, i had to cd into /challenge. By running "ls -l", 2 files were visible. the flag was in the file "24044-renamed-run-24850".

## touching files

to get the flag, we just needed to follow the instructions. run "touch /tmp/pwn" & "touch /tmp/college". after that, running /challenge/run gave the flag.

## removing files

to get the flag, i just needed to delete the "delete_me" file by running "rm delete_me" as i was already in the home directory. running /challenge/check gave the flag.

## hidden files

i changed the directory to "/". then by running ls -a, i found a file .flag-284462022125135. running cat .flag-284462022125135 gave me the flag.

## an epic filesystem quest

since it was a pretty long challenge, i'll post the terminal log here.

```
fhacker@commands~finding-files:~$ find / -name flag
find: ‘/root’: Permission denied
find: ‘/proc/1/task/1/fd’: Permission denied
find: ‘/proc/1/task/1/fdinfo’: Permission denied
find: ‘/proc/1/task/1/ns’: Permission denied
find: ‘/proc/1/fd’: Permission denied
find: ‘/proc/1/map_files’: Permission denied
Connected!                                                                        
hacker@commands~an-epic-filesystem-quest:~$ cd /
hacker@commands~an-epic-filesystem-quest:/$ ls -l
total 84
-rw-r--r--    1 root root  224 Oct 15 16:13 TEASER
lrwxrwxrwx    1 root root    7 May 30 02:03 bin -> usr/bin
drwxr-xr-x    1 root root 4096 Apr 15  2020 boot
drwxr-xr-x    1 root root 4096 Oct 15 16:13 challenge
drwxr-xr-x    6 root root  380 Oct 15 16:13 dev
drwxr-xr-x    1 root root 4096 Oct 15 16:13 etc
-r--------    1 root root   58 Oct 15 16:13 flag
drwxr-xr-x    1 root root 4096 Oct  4 23:05 home
lrwxrwxrwx    1 root root    7 May 30 02:03 lib -> usr/lib
lrwxrwxrwx    1 root root    9 May 30 02:03 lib32 -> usr/lib32
lrwxrwxrwx    1 root root    9 May 30 02:03 lib64 -> usr/lib64
lrwxrwxrwx    1 root root   10 May 30 02:03 libx32 -> usr/libx32
drwxr-xr-x    1 root root 4096 May 30 02:03 media
drwxr-xr-x    1 root root 4096 May 30 02:03 mnt
drwxr-xr-x    4 root root 4096 Sep  6 16:54 nix
drwxr-xr-x    1 root root 4096 Sep  6 16:43 opt
dr-xr-xr-x 2632 root root    0 Oct 15 16:13 proc
drwx------    1 root root 4096 Sep  6 16:44 root
drwxr-xr-x    1 root root 4096 Oct 15 16:13 run
lrwxrwxrwx    1 root root    8 May 30 02:03 sbin -> usr/sbin
drwxr-xr-x    1 root root 4096 May 30 02:03 srv
dr-xr-xr-x   13 root root    0 Sep 16 00:15 sys
drwxrwxrwt    1 root root 4096 Oct 15 16:13 tmp
drwxr-xr-x    1 root root 4096 Sep  6 16:19 usr
drwxr-xr-x    1 root root 4096 May 30 02:07 var
hacker@commands~an-epic-filesystem-quest:/$ cat TEASER 
Yahaha, you found me!
The next clue is in: /usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES

The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
hacker@commands~an-epic-filesystem-quest:/$ cd /usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES
hacker@commands~an-epic-filesystem-quest:/usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES$ ls -a
.  ..  .CLUE  vim.mo
hacker@commands~an-epic-filesystem-quest:/usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES$ cat .CLUE
Congratulations, you found the clue!
The next clue is in: /usr/lib/llvm-10/lib/clang

Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
hacker@commands~an-epic-filesystem-quest:/usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES$ ls /usr/lib/llvm-10/lib/clang
10  10.0.0  TRACE-TRAPPED
hacker@commands~an-epic-filesystem-quest:/usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES$ cat /usr/lib/llvm-10/lib/clang/TRACE-TRAPPED
Yahaha, you found me!
The next clue is in: /usr/local/lib/python3.8/dist-packages/jedi/third_party/typeshed/stdlib/3/concurrent/futures

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
hacker@commands~an-epic-filesystem-quest:/usr/share/vim/vim81/lang/ja.euc-jp/LC_MESSAGES$ cd /usr/local/lib/python3.8/dist-packages/jedi/third_party/typeshed/stdlib/3/concurrent/futures
hacker@commands~an-epic-filesystem-quest:/usr/local/lib/python3.8/dist-packages/jedi/third_party/typeshed/stdlib/3/concurrent/futures$ ls -a
.  ..  INSIGHT  __init__.pyi  _base.pyi  process.pyi  thread.pyi
hacker@commands~an-epic-filesystem-quest:/usr/local/lib/python3.8/dist-packages/jedi/third_party/typeshed/stdlib/3/concurrent/futures$ cat INSIGHT 
Tubular find!
The next clue is in: /usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__
hacker@commands~an-epic-filesystem-quest:/usr/local/lib/python3.8/dist-packages/jedi/third_party/typeshed/stdlib/3/concurrent/futures$ cd /usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__$ ls -a
.  ..  LEAD  __init__.cpython-38.pyc  apipkg.cpython-38.pyc  iniconfig.cpython-38.pyc
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__$ cd LEAD 
ssh-entrypoint: cd: LEAD: Not a directory
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__$ cat LEAD 
Congratulations, you found the clue!
The next clue is in: /opt/busybox/busybox-1.33.2/include/config/gzip
hacker@commands~an-epic-filesystem-quest:/usr/lib/python3/dist-packages/py/_vendored_packages/__pycache__$ cd /opt/busybox/busybox-1.33.2/include/config/gzip
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/gzip$ ls -a
.  ..  MESSAGE  fast.h
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/gzip$ cat MESSAGE 
Tubular find!
The next clue is in: /var/lib/aspell

Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/gzip$ ls /var/lib/aspell
HINT-TRAPPED  README
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/gzip$ cat /var/lib/aspell/HINT-TRAPPED
Yahaha, you found me!
The next clue is in: /usr/share/doc/python3-zope.interface

The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
hacker@commands~an-epic-filesystem-quest:/opt/busybox/busybox-1.33.2/include/config/gzip$ cd /usr/share/doc/python3-zope.interface
hacker@commands~an-epic-filesystem-quest:/usr/share/doc/python3-zope.interface$ ls -a
.  ..  README.rst  TIP  changelog.Debian.gz  copyright
hacker@commands~an-epic-filesystem-quest:/usr/share/doc/python3-zope.interface$ cat TIP
Tubular find!
The next clue is in: /usr/share/racket/pkgs/scribble-lib/scribble/base

The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
hacker@commands~an-epic-filesystem-quest:/usr/share/doc/python3-zope.interface$ cd /usr/share/racket/pkgs/scribble-lib/scribble/base
hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/scribble-lib/scribble/base$ ls -a
.  ..  .ALERT  compiled  lang  lang.rkt
hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/scribble-lib/scribble/base$ cat .ALERT
CONGRATULATIONS! Your perserverence has paid off, and you have found the flag!
It is: pwn.college{krwKqVyv2CBI0pgD1hfELvC6KyN.dljM4QDL0MDM2czW}

```

## making directories

to get the flag, we needed to run -> mkdir /tmp/pwn, then cd /tmp/pwn, and then create college by running touch college.
running /challenge/run gave me the flag.

## finding files

i ran the command "find / -name flag". the command outputted a list of files, most of which were inaccessible to me. I found the flag in the first try, by running the command cat /opt/aflplusplus/nyx_mode/QEMU-Nyx/default-configs/flag.

flag : pwn.college{Q7bU8fgNIDRzBkddO3hxK1F8bN5.dJzM4QDL0MDM2czW}

## linking flags

to create a symbolic link, i ran the command "ln -s /flag /home/hacker/not-the-flag" which linked the file to /flag.

running /challenge/catflag gave me the flag.

