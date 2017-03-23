#zamiast poprawiac kod mozna bylo uzyc biblioteki six,dzieki
#ktorej kod bedzie dzialal na Python2 i Python3
#import six



def generuj_klucz(key):
                     #prosciej S=range(256)
                    # w python3 range to generator obiektow - nie zwraca listy
                    #trzeba przekonwertowac na liste

    S=list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        a,b = S.index(i), S.index(j)    #swap
        S[a], S[b] = S[b], S[a]  #prosciej nizej

    return S

def generator(S):
    i = 0
    j = 0
    while True:
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j],S[i] # swap
        K = S[(S[i] + S[j]) % 256]
        yield K #jak return ale zwraca generator
                #tworzenie generatora(bo zamaist return
                #yield
        #generatory -mozliwe wznowienie funkcji w miejscu w
        #ktorym go opuscilismy,zmienne lokalne nie sa niszczone przy
        #opuszczaniu funkcji
        #generatory - funkcje ktorych dzialanie mozna wstrzymac i wznawiac
        #przy wywolywaniu nie jest zwracaana wartosc funkncji ale obiekt
        #generatora


def RC4(key):
    S = generuj_klucz(key)
    return generator(S)

if __name__ == '__main__':

    key = 'Secret'
    plaintext = 'Attack at dawn'

    def konwertuj_klucz(s):             #zamiana 'stringow' na inty w kluczu
        return [ord(c) for c in s]


    key = konwertuj_klucz(key)

    szyfr = RC4(key)

    #print 99 is equivalent to:
    #import sys
    #sys.stdout.write(str(99) + '\n')

    #'02x' % (number)  == zamiana na HEX liczby

    import sys

    for c in plaintext:
        # w python3 zamiast szyfr.next() uzywamy szyfr.__next__()
        # lub next(szyfr)
        sys.stdout.write("%02X" % (ord(c) ^ next(szyfr)))  # ^ to xor

        #jest rowniez wbudowana w pythona funkcja xor:
        #from operator import xor
        # xor(bool(a), bool(b))