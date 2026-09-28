"""This module encrypts a text with the Caesar cipher."""


def encrypt():
    """
    reads a plain text and a key and prints the encrypted text
    :return: None
    """
    plain_text = input('Klartext: ')
    upper_text = plain_text.upper()


if __name__ == '__main__':
    encrypt()