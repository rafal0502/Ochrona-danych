import binascii

from Crypto.Cipher import ARC4

cipher = ARC4.new("Key") #szyfr (generacja klucza?)
#encrypted = cipher.encrypt("Plaintext") #zaszyfrowany (encrypt=szyfrowanie)


#cipher-method(algorithm) used for encryption of some text

def convert_key(s):
    return [ord(c) for c in s]

#encrypted=convert_key(encrypted)

with  open('test.txt') as file:
    with open("encryptRC4_with_file.txt", "w") as encryptfile:
        for line in file:
            for ch in line:
                encryptfile.write(format(ord(cipher.encrypt(ch)),'02X'))






