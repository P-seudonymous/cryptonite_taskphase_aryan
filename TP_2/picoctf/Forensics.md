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



## m00nwalk

Flag: ```picoCTF{beep_boop_im_in_space}```

Hints Used: 1 & 2

This challenge was a little complicated, due to all the packages involved to get the flag.

It was clear from the hint 1 that we need to decode the .wav file using SSTV(slow scan tv) protocol. To decode this,
i installed around 3 packages related to sstv(slowrx, sstv, qsstv), out of which only qsstv worked.

Now, to give the input .wav, i tried adding the .wav direcly instead of taking input from the sound card, but
that did not work, maybe due to some error in the application.

So, i made a virtual audio channel and played the ```message.wav``` file via the channel.

i used ```pavucontrol``` as the audio server.

Here are the commands used(for giving the input):

```
pactl load-module module-null-sink sink_name=virtual-cable
paplay -d virtual-cable message.wav
```
For cleanup: 
```
>>pactl list short modules
1       libpipewire-module-rt   {
            nice.level    = -11
            rt.prio       = 88
            #rt.time.soft = -1
            #rt.time.hard = -1
            #uclamp.min = 0
            #uclamp.max = 1024
        }
2       libpipewire-module-protocol-native      {
            # List of server Unix sockets, and optionally permissions
            #sockets = [ { name = "pipewire-0" }, { name = "pipewire-0-manager" } ]
        }
4       libpipewire-module-profiler
6       libpipewire-module-metadata
8       libpipewire-module-spa-device-factory
10      libpipewire-module-spa-node-factory
12      libpipewire-module-client-node
14      libpipewire-module-client-device
16      libpipewire-module-portal
17      libpipewire-module-access       {
            # Socket-specific access permissions
            #access.socket = { pipewire-0 = "default", pipewire-0-manager = "unrestricted" }

            # Deprecated legacy mode (not socket-based),
            # for now enabled by default if access.socket is not specified
            #access.legacy = true
        }
18      libpipewire-module-adapter
20      libpipewire-module-link-factory
22      libpipewire-module-session-manager
536870912       module-always-sink
536870913       module-device-manager
536870914       module-device-restore
536870915       module-stream-restore
536870916       module-null-sink        sink_name=virtual-cable

>>pactl unload-module 536870916

pseudonymous  …/cryptonite_taskphase_aryan/TP_2/chal_assets   main !?    v14.2.1  00:48  pactl list short modules1       libpipewire-module-rt   {
            nice.level    = -11
            rt.prio       = 88
            #rt.time.soft = -1
            #rt.time.hard = -1
            #uclamp.min = 0
            #uclamp.max = 1024
        }
2       libpipewire-module-protocol-native      {
            # List of server Unix sockets, and optionally permissions
            #sockets = [ { name = "pipewire-0" }, { name = "pipewire-0-manager" } ]
        }
4       libpipewire-module-profiler
6       libpipewire-module-metadata
8       libpipewire-module-spa-device-factory
10      libpipewire-module-spa-node-factory
12      libpipewire-module-client-node
14      libpipewire-module-client-device
16      libpipewire-module-portal
17      libpipewire-module-access       {
            # Socket-specific access permissions
            #access.socket = { pipewire-0 = "default", pipewire-0-manager = "unrestricted" }

            # Deprecated legacy mode (not socket-based),
            # for now enabled by default if access.socket is not specified
            #access.legacy = true
        }
18      libpipewire-module-adapter
20      libpipewire-module-link-factory
22      libpipewire-module-session-manager
536870912       module-always-sink
536870913       module-device-manager
536870914       module-device-restore
536870915       module-stream-restore
```

Following files are attached which are the output of the decoding.

![alt text](assets/moonwalk.png)
![alt text](/assets/moonwalk_tp2.png)

