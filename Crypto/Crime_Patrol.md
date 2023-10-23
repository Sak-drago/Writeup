# Height Of Joeys Plane
How to track an entire plane just through a single image.
## Category
**OSINT**
## Points
**299**
## Challange Description
Gotham hates me. 40 bytes of secret is all I need to bring it down. Can you find my secret?
`nc ctf.d4rkc0de.iiitd.edu.in 30008`
## Attached file

## Explaination
On searching about CRIME attacks, a video pops up regarding a CTF question in PicoCTF named Compress and Decompress. On researching a bit more. We learn the direct method to solve this question!

In the Encrypt.py we have been given, key and secret. This bascically the message, that is the key on website compresses the message with string `":::"+(secret)+":::"+(message)` where secret and message are variable
It then compresses it   and then returns a list of characters which have been encrypted under `aes`.

We just need to create a decrypter python file which automatically connects to the website and decrypts the encrypted message.
I wrote the following python code after reading codes and understanding them from different websites:

## Decrypt code


And we now have the flag!
![image](https://github.com/Sak-drago/Writeup/assets/116898248/8173b99d-1649-4f95-ac3e-cced03d15892)

## Flah
```d4rk{satark_rahein_surakshit_rahein}c0de```
