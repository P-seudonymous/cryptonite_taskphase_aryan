## Cookies

Flag: ```picoCTF{3v3ry1_l0v3s_c00k135_bb3b3535}```

Hint: NONE

This chal was a little painful since i had to brute 18 cookie requests.

could have written a script in python but i dont have enough knowledge as to give requests to websites.
used cookie-manager, a browser extension to brute the requests.

funnily, i found a site, https://www.allrecipes.com/gallery/most-popular-types-of-cookies/ , which had all the cookies in order, ie macaron is 19 in this list and in the chal, and this is true for almost all the cookies.

this was the final flag.
![ALT TEXT](/assets/cookies_tp2.png)

## Forbidden Paths

Flag: ```picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}```

Hints used: NONE

In this challenge, i wasted a lot of time inspecting the html page, but then i realized that i can edit the file path directly via the textbox.

since the file was supposedly in ```/usr/share/nginx/html/```, that meant i needed to go back 4 directories, so running ```../../../../flag.txt``` gave me the flag.

The flag is attached.

![forbidden](/assets/forbidden_tp2.png)


## SOAP

Flag: ```picoCTF{XML_3xtern@l_3nt1t1ty_0dcf926e}```

Hints Used: 1

This is by far the most complicated challenge, since it required a lot of external tools to solve, and i could not get the browser is burpsuite(i used zaproxy) to run at all.

We had to perform an XXE injection, and the process was that, you need to send a GET request to the picoctf link.
from there, you needed to send a POST request on the site, by clicking a button for details of each block.

After that, you get an option to edit the xml code, where we inject the xxe.
![post](/assets/SOAP1.png)


the code that was to be added was ```<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe; 1</ID></data>```

After sending the request for the same, i got a dump of etc/passwd which contained the flag.


