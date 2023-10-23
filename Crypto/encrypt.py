import zlib
from Crypto.Cipher import AES
import random

# secret regex: a-zA-Z0-9_{}-

key = b'fakekey'
secret = "fakesecret"

def compress_func(inp):
    return zlib.compress(inp.encode())

def encrypt(message):
    pt = ":::"+secret+":::"+message
    compa = compress_func(pt)
    iv = [random.randint(0, 255) for i in range(16)]
    iv = bytes(iv)
    aes = AES.new(key, AES.MODE_CFB, iv=iv)
    encd = aes.encrypt(compa)
    return list(iv + encd)

if __name__ == "__main__":
    while True:
        print("Enter the message")
        message = input()
        print(encrypt(message))