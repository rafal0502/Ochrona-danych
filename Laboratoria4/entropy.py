import string, math
alfabetm = 'abcdefghijklmnopqrstuvwxyz'
alfabetd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabets = '!"#$%&\'()*+-./:;<=>?@[\]^_`{|}~'
alfabetc = '0123456789'

czyKoniec = False

while czyKoniec == False:
	#tekst = open('zaszyfrowany.txt').read()
	tekst = raw_input('Podaj haslo:\n')
	male = False
	duze = False
	specjalne = False
	cyfry = False

	ileAlfabetow = 0
	alpha = ''

	for char in tekst:
		if ord(char) >= 65 and  ord(char) <= 90:
			duze = True
		if ord(char) >= 97 and ord(char) <= 122:
			male = True
		if ord(char) >= 33 and ord(char) <= 47:
			specjalne = True
		if ord(char) >= 58 and ord(char) <= 64:
			specjalne = True
		if ord(char) >= 91 and ord(char) <= 96:
			specjalne = True
		if ord(char) >= 123 and ord(char) <= 126:
			specjalne = True
		if ord(char) >= 48 and ord(char) <= 57:
			cyfry = True

	if male == True:
	#	ileAlfabetow+=1
		alpha += alfabetm
	if duze == True:
	#	ileAlfabetow+=1
		alpha += alfabetd
	if specjalne == True:
	#	ileAlfabetow+=1
		alpha += alfabets
	if cyfry == True:
	#	ileAlfabetow+=1
		alpha += alfabetc

	ileZnakow = len(alpha)
	entropyPerChar = math.log (ileZnakow, 2)
	entropy = len(tekst) * entropyPerChar

	print len(tekst)
	print "Entropia na znak wynosi % 0.2f" % entropyPerChar
	print "Entropia tekst wynosi %0.2f" % entropy
