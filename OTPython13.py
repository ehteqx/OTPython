#!/usr/bin/python
# -*- coding: ascii -*-

from sys import *

intro = """
==========================================================
### OTPython v. 1.3 ASCII ###
-- A fast and lightweight Gilbert Vernam's One Time Pad cipher implementation in Python --

Code and algorithm version: 1.3
Dictionary version: 1.3 ASCIIpy (93)

Code written in Python with Sublime Text 3

(C)2014 by EMANUELE BALLARIN - All rights reserved. (e-mail: ehteqx@gmail.com)

==========================================================

"""

module_length = 93

print('Specify the path (absolute or relative) of the text file that you want to encrypt/decrypt...')
srcpath = raw_input('Source path: ')
print(' ')

while srcpath == '':
        print('Specify the path (absolute or relative) of the text file that you want to encrypt/decrypt...')
        srcpath = raw_input('Source path: ')
        print(' ')

print('Specify the path (absolute or relative) of the text file that you want to use as the cryptographic key... Note that the key has to be as long as the text file that you want to encrypt/decrypt.')
keypath = raw_input('Key path: ')
print(' ')

while keypath == '':
        print('Specify the path (absolute or relative) of the text file that you want to use as the cryptographic key... Note that the key has to be as long as the text file that you want to encrypt/decrypt.')
        keypath = raw_input('Key path: ')
        print(' ')

print('Specify whether you want to encrypt (e) or decrypt (d) the file...')
action = raw_input('Encrypt (e) or Decrypt (d): ')
print(' ')

while action != 'e' and action != 'd':
        print('Specify whether you want to encrypt (e) or decrypt (d) the file...')
        action = raw_input('Encrypt (e) or Decrypt (d): ')
        print(' ')


def encrypt(fsrcpath,fkeypath):
	input = open(fsrcpath,'r').read()
	fkey = open(fkeypath,'r').read()
	output = ''
	x = 0

	while x < len(input):
		if input[x] != '\n':
			try:
				output = output+revdict[dictionary[input[x]]+dictionary[fkey[x]]]
			except:
				output = output+revdict[dictionary[input[x]]+dictionary[fkey[x]]-module_length]
		else:
			output = output+'\n'
		x += 1
	newFile = open('Encrypted_File.txt','w')
	newFile.write(output)
	newFile.close()

	print('Your text file has been successfully encrypted and saved as "Encrypted_File.txt"')


def decrypt(fsrcpath,fkeypath):
	input = open(fsrcpath,'r').read()
	fkey = open(fkeypath,'r').read()
	output = ''
	x = 0

	while x < len(input):
		if input[x] != '\n':
			try:
				output = output+revdict[dictionary[input[x]]-dictionary[fkey[x]]]
			except:
				output = output+revdict[dictionary[input[x]]-dictionary[fkey[x]]+module_length]
		else:
			output = output+'\n'
		x += 1
	newFile = open('Decrypted_File.txt','w')
	newFile.write(output)
	newFile.close()

	print('Your text file has been successfully decrypted and saved as "Decrypted_File.txt"')


dictionary = {' ':0,'!':1,'"':2,'#':3,'$':4,'%':5,'&':6,'(':7,')':8,'*':9,'+':10,',':11,'-':12,'.':13,'/':14,'0':15,'1':16,'2':17,'3':18,'4':19,'5':20,'6':21,'7':22,'8':23,'9':24,':':25,';':26,'<':27,'=':28,'>':29,'?':30,'@':31,'A':32,'B':33,'C':34,'D':35,'E':36,'F':37,'G':38,'H':39,'I':40,'J':41,'K':42,'L':43,'M':44,'N':45,'O':46,'P':47,'Q':48,'R':49,'S':50,'T':51,'U':52,'V':53,'W':54,'X':55,'Y':56,'Z':57,'[':58,']':59,'^':60,'_':61,'`':62,'a':63,'b':64,'c':65,'d':66,'e':67,'f':68,'g':69,'h':70,'i':71,'j':72,'k':73,'l':74,'m':75,'n':76,'o':77,'p':78,'q':79,'r':80,'s':81,'t':82,'u':83,'v':84,'w':85,'x':86,'y':87,'z':88,'{':89,'|':90,'}':91,'~':92}
revdict = {}
for dictval, val in dictionary.iteritems():
	revdict[val] = dictval


if action == 'e':
	try:
		encrypt(srcpath,keypath)
	except:
		print('Something went wrong while encrypting/decrypring your text file! Please, try again. Check if the paths that you have specified are correct and that the files that you want to encrypt/decrypt (or use as key) both exist. Please note: the key must be as long as the text that you want to encrypt/decrypt.')
elif action == 'd':
	try:
		decrypt(srcpath,keypath)
	except:
		print('Something went wrong while encrypting/decrypring your text file! Please, try again. Check if the paths that you have specified are correct and that the files that you want to encrypt/decrypt (or use as key) both exist. Please note: the key must be as long as the text that you want to encrypt/decrypt.')
else:
    print('Something went wrong while encrypting/decrypring your text file! Please, try again. Check if the paths that you have specified are correct and that the files that you want to encrypt/decrypt (or use as key) both exist. Please note: the key must be as long as the text that you want to encrypt/decrypt.')

print(' ')
print(' ')
print('Bye bye!')
print('Thank you for having used OTPtyhon!')