## learning from documentation

running ```/challenge/challenge --giveflag``` gave the flag.

## learning complex usage

running the following command ```/challenge/challenge --printfile /flag``` gave me the flag.

## reading manuals

to get the flag, i first ran ```man challenge``` which gave me the manual for challenge.

![alt text](/assets/manuals.png "")

running the command ```/challenge/challenge --fmnwwf 391``` gave me the flag.

## searching manuals

this challenge was pretty similar to the last one. we just needed to search for flag by ```/flag``` and then using ```N``` or ```n``` to see the results.

```challenge/challenge --jekl``` gave the flag.

## searching for manuals

after running the command ```man man```, i spotted ```man -k [apropos options] regexp ...```
apropos is a command used to find a command using the manual page.

after that, i ran ```man -h``` to cross-check/reverify the arguments for apropos.
since i know the format of the command, i ran ```man -k challenge``` which returned the command name of challenge.

the final command for the flag was ```/challenge/challenge --kvbntq 998```
below is the terminal log of the challenge.

```
hacker@man~searching-for-manuals:~$ man man
MAN(1)                                         Manual pager utils                                         MAN(1)

NAME
       man - an interface to the system reference manuals

SYNOPSIS
       man [man options] [[section] page ...] ...
       man -k [apropos options] regexp ...
       man -K [man options] [section] term ...
       man -f [whatis options] page ...
       man -l [man options] file ...
       man -w|-W [man options] page ...

DESCRIPTION
       man  is  the  system's  manual pager.  Each page argument given to man is normally the name of a program,
       utility or function.  The manual page associated with each of these arguments  is  then  found  and  dis‐
       played.  A section, if provided, will direct man to look only in that section of the manual.  The default
       action is to search in all of the available sections following a pre-defined order (see DEFAULTS), and to
       show only the first page found, even if page exists in several sections.

       The table below shows the section numbers of the manual followed by the types of pages they contain.

       1   Executable programs or shell commands
       2   System calls (functions provided by the kernel)
       3   Library calls (functions within program libraries)
       4   Special files (usually found in /dev)
       5   File formats and conventions, e.g. /etc/passwd
       6   Games
       7   Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7)
       8   System administration commands (usually only for root)
       9   Kernel routines [Non standard]

       A manual page consists of several sections.

hacker@man~searching-for-manuals:~$ man -h
Usage: man [OPTION...] [SECTION] PAGE...

  -C, --config-file=FILE     use this user configuration file
  -d, --debug                emit debugging messages
  -D, --default              reset all options to their default values
      --warnings[=WARNINGS]  enable warnings from groff

 Main modes of operation:
  -f, --whatis               equivalent to whatis
  -k, --apropos              equivalent to apropos
  -K, --global-apropos       search for text in all pages
  -l, --local-file           interpret PAGE argument(s) as local filename(s)
  -w, --where, --path, --location
                             print physical location of man page(s)
  -W, --where-cat, --location-cat
                             print physical location of cat file(s)

  -c, --catman               used by catman to reformat out of date cat pages
  -R, --recode=ENCODING      output source page encoded in ENCODING

 Finding manual pages:
  -L, --locale=LOCALE        define the locale for this particular man search
  -m, --systems=SYSTEM       use manual pages from other systems
  -M, --manpath=PATH         set search path for manual pages to PATH

  -S, -s, --sections=LIST    use colon separated section list

  -e, --extension=EXTENSION  limit search to extension type EXTENSION

  -i, --ignore-case          look for pages case-insensitively (default)
  -I, --match-case           look for pages case-sensitively

      --regex                show all pages matching regex
      --wildcard             show all pages matching wildcard

      --names-only           make --regex and --wildcard match page names only,
                             not descriptions

  -a, --all                  find all matching manual pages
  -u, --update               force a cache consistency check

      --no-subpages          don't try subpages, e.g. 'man foo bar' => 'man
                             foo-bar'

 Controlling formatted output:
  -P, --pager=PAGER          use program PAGER to display output
  -r, --prompt=STRING        provide the `less' pager with a prompt

  -7, --ascii                display ASCII translation of certain latin1 chars
  -E, --encoding=ENCODING    use selected output encoding
      --no-hyphenation, --nh turn off hyphenation
      --no-justification,                              --nj   turn off justification
  -p, --preprocessor=STRING  STRING indicates which preprocessors to run:
                             e - [n]eqn, p - pic, t - tbl,
g - grap, r - refer, v - vgrind

  -t, --troff                use groff to format pages
  -T, --troff-device[=DEVICE]   use groff with selected device

  -H, --html[=BROWSER]       use www-browser or BROWSER to display HTML output
  -X, --gxditview[=RESOLUTION]   use groff and display through gxditview
                             (X11):
                             -X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
  -Z, --ditroff              use groff and force it to produce ditroff

  -?, --help                 give this help list
      --usage                give a short usage message
  -V, --version              print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.

Report bugs to cjwatson@debian.org.
hacker@man~searching-for-manuals:~$ man -k challenge
kvbntqhnxm (1)       - print the flag!
hacker@man~searching-for-manuals:~$ man kvbntqhnxm

CHALLENGE(1)                                   Challenge Commands                                   CHALLENGE(1)

NAME
       /challenge/challenge - print the flag!

SYNOPSIS
       challenge OPTION

DESCRIPTION
       Output the flag when called with the right arguments.

       --fortune
              read a fortune

       --version
              output version information and exit

       --kvbntq NUM
              print the flag if NUM is 998

AUTHOR
       Written by Zardus.

REPORTING BUGS
       The repository for this dojo: <https://github.com/pwncollege/linux-luminarium/>

SEE ALSO
       man(1) bash-builtins(7)

pwn.college                                         May 2024                                        CHALLENGE(1)
hacker@man~searching-for-manuals:~$ /challenge/challenge --kvbntq 998
Correct usage! Your flag: pwn.college{M9kvKEA9bntqHS_I8M6hBnxmGxv.dZTM4QDL0MDM2czW}
```


## Helpful programs

running the command ```/challenge/challenge -h``` gave the list of arguments for the command.

![alt text](/assets/helpful_programs.png "")

the following code shows the procedure of arriving at the flag.
the final command was ```/challenge/challenge -g 205```

## help for builtins
the following code snippet shows the procedure of getting the flag.
the final command was ```challenge --secret wOVUX75n``` as the rest of the arguments returned irrelavent values.

![alt text](/assets/builtins.png "")



