'''
Ceasar Cypher
Encrypt messages by shifting the letters
Had some help using example given on Sololearn: https://code.sololearn.com/cK267fizDS8H/#py
'''
import string


plain = string.ascii_letters # alphabet
shift = int(input('Shift by: ')) # Enter the rotation 
message = input('Encrypt: ') # Message user want's to ecrypt
print() 


def encrypt_message(shift, message): # function that generates the encrypted message based on shift input
    encrypt_message = ''

    for letter in message:
        i = (plain.index(letter) + shift) % 52
        encrypt_message += plain[i] # set encrypted message equal to the rotation

    return 'Encrypted message: {}'.format(encrypt_message)


def decrypt_message(shift, encrypt): # function decrypts the encrypted message
    decrypted_message = ''

    for letter in encrypt:
        try:
            i = (plain.index(letter) - shift) % 52
            decrypted_message += plain[i]
        except ValueError: # added Value error because there was a value error
            decrypted_message += letter

    return 'Decrypted: {}'.format(decrypted_message)

encrypted = encrypt_message(shift, message)
print(encrypted)

decrypted = decrypt_message(shift, encrypted)
print(decrypted)