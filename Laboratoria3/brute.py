#!/usr/bin/python
from __future__ import division
import itertools
import string
import sys, re, string
import math
import six
from Crypto.Cipher import ARC4

alfabet = 'abcdefghijklmnopqrstuvwxyz'

def entropy(text):
	stat = {}
	pznak = {}
	n = 0
	for znak in text:
		if znak in stat:
			stat[znak] += 1
		else:
			stat[znak] = 1
		n += 1
	for znak in stat:
		pznak[znak] = stat[znak]/n
	entropy = 0
		#print "%s <=> %d" % (znak, stat[znak])
	for znak in pznak:
		#print "%s <=> %f" % (znak, pznak[znak])
		entropy += - math.log (pznak[znak],2)*pznak[znak] 	
	return entropy

#cipher = ARC4.new("dfgh")

#fi = open(sys.argv[1],'rb')
#text = fi.readline()
#plaintext = cipher.encrypt(text)

#plik = open('plik.txt','rb')

#for line in plik.readlines():
#	key = ''
#	key = line
#	print key
#	cipher = ARC4.new(key)
#	decrypted = cipher.decrypt(text)
	#print entropy(decrypted)
#	if(entropy(decrypted)) < 4.5:
#		print key
#		print entropy(decrypted)
def brute(encrypted):
	key = ''
	for first in range(0,26):
    		for second in range (0,26):
        		for third in range(0,26):
            			key = chr(ord('a')+first)+chr(ord('a')+second)+chr(ord('a')+third)
            			cipher = ARC4.new(key)
            			decrypted = cipher.encrypt(encrypted)
				if decrypted.startswith(b'\xff\xd8'):
					print key
					return
	print "Key not found"
	return		

            		#if (entropy(decrypted)) < 3.6:
               		#	print key
               		#	print entropy(decrypted)
def do():
	file = open(sys.argv[1],'rb')
	text = file.read()
	brute(text)

if __name__ == '__main__':
	do()