# Crime_Patrol
How to track an entire plane just through a single image.
## Category
**CRIMEANDBEASTATTACK**
## Points
**300**
## Challange Description
Gotham hates me. 40 bytes of secret is all I need to bring it down. Can you find my secret?
`nc ctf.d4rkc0de.iiitd.edu.in 30008`
## Attached file
[encrypt.py](https://github.com/Sak-drago/Writeup/blob/main/Crypto/encrypt.py)

## Explaination
On searching about CRIME attacks, a video pops up regarding a CTF question in PicoCTF named Compress and Decompress. On researching a bit more. We learn the direct method to solve this question!

In the Encrypt.py we have been given, key and secret and Zlib. 

Zlib uses string compression where it uses DEFLATE Algorithm to compress the string.
From figuring that out, we know what the string will have `d4rk` as part of its solution.
Now, we use trial and error to figure out the output
For example, using a dummy flag, `d4rk{xyz}c0de`.
If we try to input `d4rk{a` then we get 6 bytes but if we input `d4rk{xy` we get 7 bytes (*This is because AES gives us the length of the string*)

This bascically the message, that is the key on website compresses the message with string `":::"+(secret)+":::"+(message)` where secret and message are variable
### Check the file.
It then compresses it   and then returns a list of characters which have been encrypted under `aes`.

From figuring that out, we know what the string will have `d4rk` as part of its solution.
Now, we use trial and error to figure out the output

We just need to create a trial and error python file which automatically connects to the website and decrypts the encrypted message.
I wrote the following python code after reading codes and understanding them from different websites:

## Python code
```python
from pwn import *
import string

r = remote("localhost", 30008)
valid_chars = string.ascii_letters + string.digits + "_{}"
solution_so_far = ""

while len(solution_so_far) < 40:
    best = ''
    best_len = 99999999
    for c in valid_chars:
        test = solution_so_far + c
        test = bytes(test, "utf-8")
        r.recvuntil(b"message")
        r.sendline(test)
        r.recvline()
        ans = r.recvline().decode().strip()
        ans = ans[1:-1]
        ans = ans.split(",")
        lenofencode = len(ans)

        if lenofencode < best_len:
            best_len = lenofencode
            best = c

    if best is None:
        break

    solution_so_far += best

print(solution_so_far)
```
The above code guesses the elements and thus guves us a final result after running trial and error!
***NOTE***: NetCat (nc)

`nc` or `NetCat` allows us to connect to a port/server from our device!
In the question, we are given `nc ctf.d4rkc0de.iiitd.edu.in 30008` which means we have to connect to remote port.
Here, 'ctf.d4rkc0de.iiitd.edu.in' is the server and '30008' is the port we're connecting to!
We have to do this because the Flag is actually on the server and not on our side.

And on running the file, we recieve the flag!
![image](https://github.com/Sak-drago/Writeup/assets/116898248/8173b99d-1649-4f95-ac3e-cced03d15892)

## Flag
```d4rk{satark_rahein_surakshit_rahein}c0de```
