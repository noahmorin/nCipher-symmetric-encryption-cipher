# Custom Symmetric Cipher created by Noah Morin, October 15, 2021
# Th cipher reads in a plaintext and a 128-bit key (line  91 and 93) and both encrypts and decrypts the string
# the encrypted text can be found in encryptedmessage.txt
# the decrypted text can be found in decryptedmessage.txt

def n_cipher(plntxt, keystr):
    charValueList = [ord(c) for c in plntxt]  # convert plaintext into a list of decimal ascii values (i.e a -> 97)
    keyList = [ord(k) for k in keystr]  # convert plaintext key into a list of decimal ascii values
    cryptedlist = []
    keypos = 0
    encryptedString = ''
    # define two emtpy variables and an emtpy list to be used later in the function

    for v in range(len(charValueList)):  # for loop that iterated through charValueList with an integer variable v
        if charValueList[v] + (keyList[keypos]) >= 253:
            cryptedlist.append([(charValueList[v]), "x"])
        # if the decimal value of the current character in charVaulueList + the decimal value of the current key
        # character is greater than or equal to 253, assume it is not within the printable range of characters and
        # append it to the list with an "x" flag
        elif 253 > charValueList[v] + (keyList[keypos]) >= 180:
            cryptedlist.append([(charValueList[v] + (keyList[keypos] - 127)), "a"])
        # repeated step from last, else if the sum of the two decimal values are less than 253 and greater than or equal
        # to 180, append the sum of the two values - 127 with the "a" flag.
        elif 180 > charValueList[v] + (keyList[keypos]) >= 155:
            cryptedlist.append([(charValueList[v] + (keyList[keypos] - 97)), "b"])
        # repeated step from last, else if the sum of the two decimal values are less than 180 and greater than or equal
        # to 155, append the sum of the two values - 97 with the "b" flag.
        else:
            cryptedlist.append([(charValueList[v] + (keyList[keypos] - 31)), "c"])
        # repeated step from last, else the sum of the two decimal values are less than 180 and greater than or equal to
        # 155, append the sum of the two values - 97 with the "b" flag.
        if keypos < 15:
            keypos += 1
        else:
            keypos = 0
        # As the for loop cycles through the charValueList, increment through the key

    for pair in cryptedlist:  # for loop that cylces through the pairs of characters and flags in cryptedlist
        for item in pair:  # for loop that cycles through the two items in the pair
            if type(item) == int:
                # if the character in question is an integer, decode the string from a decimal to an ascii value
                # and append it to the encryptedString
                encryptedString += chr(item)
            else:
                # else, at the unencoded character to the encrypted string
                encryptedString += item

    return encryptedString  # return the encrypted string


def n_decipher(cyphrtxt, keystr):
    keyList = [ord(k) for k in keystr]  # convert plaintext key into a list of decimal ascii values
    decryptedList, cryptedList = [], []  # define two empty lists
    decryptedString = ''  # define an empty string, decryptedString
    keypos = 0  # define the keypos int variable to 0

    for char in range(0, len(cyphrtxt), 2):
        cryptedList.append([cyphrtxt[char], cyphrtxt[char + 1]])
    # iterate through the cipher text by twos, add the pair (char and flag) to the cryptedlist.

    for pair in range(len(cryptedList)):
        cryptedList[pair][0] = ord(cryptedList[pair][0])
    # iterate through the pairs in crypted list, encode the char to it's decimal ascii value

    for v in range(len(cryptedList)):  # for loop that iterates through the cryptedlist with the v variable.
        if cryptedList[v][1] == "x":  # if the character flag is "x"
            decryptedList.append(cryptedList[v][0])  # append the current character to the decryptedList
        elif cryptedList[v][1] == "a":  # if the character flag is "a"
            decryptedList.append(cryptedList[v][0] - keyList[keypos] + 127)
            # append the decimal value of the current char + the current key + 127
        elif cryptedList[v][1] == "b":  # if the character flag is "b"
            decryptedList.append(cryptedList[v][0] - keyList[keypos] + 97)
            # append the decimal value of the current char + the current key + 97
        else:  # else. # append the decimal value of the current char + the current key + 31
            decryptedList.append(cryptedList[v][0] - keyList[keypos] + 31)

        if keypos < 15:
            keypos += 1
        else:
            keypos = 0
        # As the for loop cycles through the charValueList, increment through the key

    for char in decryptedList:  # iterate through the characters in decryptedlist
        decryptedString += chr(char)  # decode the char in decrypted list to a string

    return decryptedString  # return the decrypted string


if __name__ == '__main__':
    f1 = open("plaintext.txt", "r")
    plaintext = f1.read()
    f1.close()

    f2 = open("key.txt", "r")
    keystring = f2.read()
    f2.close()
    # read the plaintext file along with the key for use in the encryption algorithm

    encryptedtext = n_cipher(plaintext, keystring)
    # call the encryption algorithm, pass the plaintext and key as parameters.

    f3 = open("encryptedmessage.txt", "w")
    f3.write(str(encryptedtext))
    f3.close()
    # write to a file, "encryptedmessage.txt" the encrypted text

    f4 = open("encryptedmessage.txt", "r")
    ciphertext = f4.read()
    f4.close()
    print(ciphertext)
    # read the encryptedmessage.txt file as variable ciphertext

    decryptedtext = n_decipher(ciphertext, keystring)
    # call the decryption algorithm to decrypt the cipher text.
    f5 = open("decryptedmessage.txt", "w")
    f5.write(decryptedtext)
    f5.close()
    # write to a file, "decryptedmessage.txt" the decrypted message
