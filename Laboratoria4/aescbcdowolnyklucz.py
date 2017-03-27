import sys
import string
from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
import itertools
import hashlib

#key = raw_input("Podaj klucz \n")

s = open(sys.argv[1]).readline()
key = sys.argv[2]
if len(s) % 16 != 0:
        reszta = len(s) % 16
        for i in range(16-reszta):
                s += 'a'


hash_object = hashlib.sha256(key)
hex_dig = hash_object.hexdigest()[:16]
print(hex_dig)

iv =  get_random_bytes(AES.block_size)

aesCBC = AES.new(hex_dig,AES.MODE_CBC, iv)

print aesCBC.encrypt(s)