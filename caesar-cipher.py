#!/usr/bin/env python

# =========================================================================== #
#    Imports
# =========================================================================== #

import argparse, sys

# =========================================================================== #
#    Functions
# =========================================================================== #

def caesar(plainText, shift, mod):
    """Encrypt a message using a Caesar Cipher """
    encryptedText = ""
    for character in plainText:
        if character.isalpha():
            newChar = chr ( ord (character) + ( ord (character) -
                ord (character) + shift ) % mod )
            encryptedText += newChar.upper()
    return encryptedText

def decrypt_caesar(plainText, shift, mod):
    """ Decrypt a message using a Caesar Cipher """
    decryptedText = ""
    for character in plainText:
        if character.isalpha():
            newChar = chr ( ord (character) - ( ord (character) -
                ord (character) + shift ) % mod )
            decryptedText += newChar.upper()
    return decryptedText

# =========================================================================== #
#    Command Line
# =========================================================================== #

parser = argparse.ArgumentParser(description="Encrypt or Decrypt a given message")
parser.add_argument("-e", "--encrypt", metavar="'Message'", help="Encrypt a message")
parser.add_argument("-d", "--decrypt", metavar="'Message'", help="Decrypt a message")
parser.add_argument("-s", "--shift", metavar="Integer for the shift", default=3, type=int, help="Give a number between 1-25 for the cipher shift (default is 3)")
parser.add_argument("-m", "--mod", metavar="Modulus divisor for the language", default=26, type=int, help="Give the modulus divisor for your language (default is 26 for English)")
args = parser.parse_args()

error = ''
if args.shift > 25:
    args.shift = 3
    error = 'You chose a shift value above 25 so the default value of 3 was used'
if args.shift < 1:
    args.shift = 3
    error = 'You chose a shift value below 1 so the default value of 3 was used'
if args.encrypt:
    print "Your encrypted text is: ",caesar(args.encrypt, args.shift, args.mod)
    if error != '':
        print error

if args.decrypt:
    print "Your decrypted text is: ",decrypt_caesar(args.decrypt, args.shift, args.mod)
    if error != '':
        print error

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
