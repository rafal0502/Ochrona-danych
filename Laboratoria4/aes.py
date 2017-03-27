import sys
import string
from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes

iv =  get_random_bytes(AES.block_size)
key = "1223344285920561"
aesCBC = AES.new(key,AES.MODE_CBC, iv)
aesECB = AES.new(key,AES.MODE_ECB, iv)

s = open(sys.argv[1]).readline()


if len(s) % 16 != 0:
	reszta = len(s) % 16
	for i in range(16-reszta):
		s += 'a'

print s
print aesCBC.encrypt(s)
print aesECB.encrypt(s)