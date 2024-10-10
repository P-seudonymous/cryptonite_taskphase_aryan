## ready player one

this challenge was simple as a .wav audio file was provided which played a morse code, which when decoded, gave the flag.

## This or that?

the clues to the flag were in the description itself. the text was ARTEMIS_WHISPER, and the key was 036363127c7c60001a117c6463170b, the encrytion method was XOR cipher.

## Knock Knock

The QR code contained the flag, which just had to get cleaned up.

## Quence your thirst

this challenge was a little tricky, due to the following factors:

the text was a mono-alphabetic substituion cipher, which when decoded, gave a katb.in link
however, the katb.in link was not decoded properly as 4 alphabets were not substituted in the cipher.

so to solve it, i matched the substituion key with the rest of the text, which gave me 4 possible letters to replace in the katb.in link.

from there, it was a simple bash, as only 4! combinations are possible, in which one was the correct link, which contained the flag.

## Git Gud

the folder contained a .gitignore folder, in which the commits were the flag.

## Stairway to heaven

in the following problem, an executable file(game) was provided, which gave an output of colors, which when copied, containted text. that text contained a string of ascii characters which was the flag.

## Heads up, tails down.

in the following challenge, a png was provided which was corrupted, inorder to fix it, i used a hex editor, and changed the 1st line of the hex code to spell out .PNG(file type) and IDAT(image data chunk).

## A rocky start

this was challenge which was a lot time consuming for me, but the solution was pretty simple.
here we were given an executable file, Asteroids, and to break the game, we needed a score of 100.
inorder to achieve that, i tried experimenting with player names, and it eventually led me to a conclusion that, a string of 26 'a's would fetch me the score 97, which in ascii, represents the char 'a'.
therefore to reach a score of 100, i gave an input of 26 'd's, which gave out the flag.

## Mo-sike

it was basically solved by giving the correct prompts to chat-gpt, which got us a somewhat understandable image of missingno, the pokemon which was the flag of the challenge.
