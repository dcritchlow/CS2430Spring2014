def encrypt(shift, plaintext):
    cipherText = ""
    for character in plaintext:
        letter = ord(character) + shift
        if letter > ord('\xff'):
            letter -= 256
        finalLetter = chr(letter)
        cipherText += finalLetter
    print "Your encrypted text is: ", cipherText
    return cipherText

def decrypt(shift, cipherText):
    plainText = ""
    for character in cipherText:
        letter = ord(character) - shift
        if letter < ord('\x00'):
            letter += 256
        finalLetter = chr(letter)
        plainText += finalLetter
    print "Your decrypted text is: ", plainText
    return plainText

def caesar(plainText, shift):
    encryptedText = ""
    for character in plainText:
        if character.isalpha():
            # print character
            # print ord(character)
            alphabetLetter = ord(character) + shift
            if character.isupper():
                if alphabetLetter < ord('A'):
                    alphabetLetter += 26
                    # print alphabetLetter
                elif alphabetLetter > ord('Z'):
                    alphabetLetter -= 26
                    # print alphabetLetter
            if character.islower():
                if alphabetLetter < ord('a'):
                    alphabetLetter += 26
                    # print alphabetLetter
                if alphabetLetter > ord('z'):
                    alphabetLetter -= 26
                    # print alphabetLetter
            finalLetter = chr(alphabetLetter)
            encryptedText += finalLetter
        if character.isspace():
            encryptedText += ' '
        # print '\n'
        # if character in string.punctuation:
        #     punctuation = ord(character) + shift
        #     if punctuation > ord('~'):
        #         punctuation -= 94
        #     finalPunctuation = chr(punctuation)
        #     encryptedText += finalPunctuation
    print "Your encrypted text is: ", encryptedText
    return encryptedText

def decrypt_caesar(plainText, shift):
    decryptedText = ""
    for character in plainText:
        # print character
        # print ord(character)
        if character.isalpha():
            alphabetLetter = ord(character) - shift
            # print alphabetLetter
            if character.isupper():
                if alphabetLetter > ord('Z'):
                    alphabetLetter -= 26
                    # print alphabetLetter
                elif alphabetLetter < ord('A'):
                    alphabetLetter += 26
                    # print alphabetLetter
            if character.islower():
                if alphabetLetter < ord('a'):
                    alphabetLetter += 26
                    # print alphabetLetter
                if alphabetLetter > ord('z'):
                    alphabetLetter -= 26
                    # print alphabetLetter
            finalLetter = chr(alphabetLetter)
            decryptedText += finalLetter
        if character.isspace():
            decryptedText += ' '
        # print '\n'
        # if character in string.punctuation:
        #     punctuation = ord(character) + shift
        #     if punctuation < ord('!'):
        #         punctuation += 94
        #     finalPunctuation = chr(punctuation)
        #     decryptedText += finalPunctuation
    print "Your decrypted text is: ", decryptedText
    return decryptedText

def caesarWithPunctuation(plainText, shift):
    encryptedText = ""
    for character in plainText:
        # print character
        letter = ord(character) + shift
        # print letter
        if letter > ord('~'):
            letter -= 95
            # print letter
        if letter < ord(' '):
            letter += 95
            # print letter
        finalLetter = chr(letter)
        # print finalLetter
        encryptedText += finalLetter
    print "Your encrypted text is: ", encryptedText
    return encryptedText

def decrypt_caesarWithPunctuation(plainText, shift):
    decryptedText = ""
    # print plainText
    for character in plainText:
        # print character
        letter = ord(character) - shift
        # print letter
        if letter < ord(' '):
            letter += 95
            # print letter
        if letter > ord('~'):
            letter -= 95
            # print letter
        finalLetter = chr(letter)
        # print finalLetter
        decryptedText += finalLetter
    print "Your decrypted text is: ", decryptedText
    return decryptedText

if __name__ == '__main__':
    import string
    plaintext = raw_input("Enter the text to encrypt\n")
    shift = int(raw_input("Enter a number (between 1-95) to shift by\n"))
    # cipherText = encrypt(shift, plaintext)
    # decrypt(shift, cipherText)
    encryptedText = caesar(plaintext,shift)
    decrypt_caesar(encryptedText, shift)

    # encryptedText = caesarWithPunctuation(plaintext, shift)
    # decrypt_caesarWithPunctuation(encryptedText, shift)
