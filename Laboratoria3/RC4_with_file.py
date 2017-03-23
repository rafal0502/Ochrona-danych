def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':
    # test vectors are from http://en.wikipedia.org/wiki/RC4

    # ciphertext should be BBF316E8D940AF0AD3
    key = 'Key'



    # ciphertext should be 1021BF0420
    #key = 'Wiki'
    #plaintext = 'pedia'

    # ciphertext should be 45A01F645FC35B383552544B9BF5
    #key = 'Secret'
    #plaintext = 'Attack at dawn'

    def convert_key(s):
        return [ord(c) for c in s]
    #funkcja ord zwraca wartosc ASCII ze znaku

    key = convert_key(key)

    keystream = RC4(key)


    with  open('test.txt') as file:
        with open("encryptRC4_with_file.txt","w") as encryptfile:
            for line in file:
                for ch in line:
                    encryptfile.write(format(ord(ch) ^ next(keystream),'02X'))
                  # formatujemy int (ord zamienia char na int) i zapisujemy w Hex
                  #  sys.stdout.write("%02X" % (ord(ch) ^ next(keystream)))-tak od razu
                  # na wyjscie mozna zapisac














