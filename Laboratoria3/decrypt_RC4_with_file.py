import base64

with open("encryptRC4_with_file.txt", "r") as encrypted_file:
    data = (encrypted_file.read()).decode("hex")
key = "Key"

S = range(256)
j = 0
out = []

#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

decrypted_text = ''.join(out)
with open('decrypted_RC4_with_file.txt', 'w') as decrypted_file:
    decrypted_file.write(decrypted_text)