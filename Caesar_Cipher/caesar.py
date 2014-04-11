#======================================================================#
#    Imports
#======================================================================#

import argparse, sys

# =====================================================================#
#    Functions
# =====================================================================#

""" Encrypt a message using a Caesar Cipher """
def caesar(plainText, shift):
    encryptedText = ""
    for character in plainText:
        if character.isalpha():
            alphabetLetter = ord(character) + shift
            if character.isupper():
                if alphabetLetter < ord('A'):
                    alphabetLetter += 26
                elif alphabetLetter > ord('Z'):
                    alphabetLetter -= 26
            if character.islower():
                if alphabetLetter < ord('a'):
                    alphabetLetter += 26
                if alphabetLetter > ord('z'):
                    alphabetLetter -= 26
            finalLetter = chr(alphabetLetter)
            encryptedText += finalLetter
        if character.isspace():
            encryptedText += ' '
    return encryptedText

""" Decrypt a message using a Caesar Cipher """
def decrypt_caesar(plainText, shift):
    decryptedText = ""
    for character in plainText:
        if character.isalpha():
            alphabetLetter = ord(character) - shift
            if character.isupper():
                if alphabetLetter > ord('Z'):
                    alphabetLetter -= 26
                elif alphabetLetter < ord('A'):
                    alphabetLetter += 26
            if character.islower():
                if alphabetLetter < ord('a'):
                    alphabetLetter += 26
                if alphabetLetter > ord('z'):
                    alphabetLetter -= 26
            finalLetter = chr(alphabetLetter)
            decryptedText += finalLetter
        if character.isspace():
            decryptedText += ' '
    return decryptedText

# =====================================================================#
#    Command Line
# =====================================================================#

parser = argparse.ArgumentParser(description="Encrypt or Decrypt a given message")
parser.add_argument("-e", "--encrypt", metavar="'Message'", help="Encrypt a message")
parser.add_argument("-d", "--decrypt", metavar="'Message'", help="Decrypt a message")
parser.add_argument("-s", "--shift", metavar="Integer for the shift", default=3, type=int, help="Give a number between 1-25 for the cipher shift (default is 3)")
args = parser.parse_args()

error = ''
if args.shift > 25:
    args.shift = 3
    error = 'You chose a shift value above 25 so the default value of 3 was used'
if args.shift < 1:
    args.shift = 3
    error = 'You chose a shift value below 1 so the default value of 3 was used'
if args.encrypt:
    print "Your encrypted text is: ",caesar(args.encrypt, args.shift)
    if error != '':
        print error

if args.decrypt:
    print "Your decrypted text is: ",decrypt_caesar(args.decrypt, args.shift)
    if error != '':
        print error

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
