"""This module encrypts a text with the Caesar cipher."""


def encrypt():
    """
    reads a plain text and a key and prints the encrypted text
    :return: None
    """
    plaintext = input('Klartext: ')
    plaintext = plaintext.upper()
    key = int(input('Schlüssel: '))
    position = 0
    while position < len(plaintext):
        chiffre = plaintext[position]
        if chiffre != ' ':
            code = ord(chiffre)
            code += key
            if code > 90:
                code -= 26
            chiffre = chr(code)
            print (chiffre)
        position += 1

if __name__ == '__main__':
    encrypt()