## Trivial Flag Transfer Protocol

Flag: ```picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}```

Hints used: NONE

This challenge was a long one, especially for me since i'm not that well versed with networking terms, like TFTP.
So it took a lot of research to understand what i had to do in this chal.

I started with installing wireshark, since it is the standard software for opening .pcapang files.

after that, i went to the TFTP column and found 6 files, which i extracted and downloaded.

Instructions.txt: ```GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA```

Went to https://dcode.fr/en/ and used cipher identifier to check what encryption method was used. ROT13 is being used here.

decrypted text: ```TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER.FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN```

opened Plan.txt: ```VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF```

decrypted text: ```I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE.CHECK OUT THE PHOTOS```

Now, i tried to open the .deb file, but since i use arch btw, i just extracted the .deb file and found it was pkg for [steghide](/TP_2/chal_assets/TFTP/program/control/control).

i installed the pgk using yay, and ran some commands(image attacted below) to get the flag

Also, i figured that the passphrase should be DUEDILIGENCE since there was no other option.

![ALT TEXT](/assets/tftp_tp2.png)



## tunn3l_v1s10n

Flag: ```picoCTF{qu1t3_a_v13w_2020}```

Hints Used: NONE

This challenge was extremely straightforward,
i ran ```xxd -l 0x40 tunn3l_v1s10n``` to get the first 4 lines of hexdump, which made it clear that i had to mess with the header file and pixel size data of the .BMP(windows bitmap) file.

The following image shows the data i edited.

![ALT TEXT](/assets/tunnel_vision_tp2.png)

The flag is attached below.

![ALT TEXT](/assets/tunn3l_v1s10n.bmp)




