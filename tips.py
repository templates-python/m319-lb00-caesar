def main():
    some_text = 'Hallo'
    pos = 1
    # Länge eines Textes ermitteln
    length = len(some_text)     # = 5
    print (f'Länge des Textes: {length}')

    # Text in Grossbuchstaben umwandeln
    upper_text = some_text.upper()   # = 'HALLO'
    print (f'Text in Grossbuchstaben: {upper_text}')

    # Einen einzelnen Buchstaben aus einem Text holen
    # Wichtig: Der erste Buchstabe hat Position 0, der zweite Buchstabe hat Position 1, ...
    some_char = some_text[2]    # = 'l'
    another = some_text[pos]    # = 'a'
    print (f'Einzelne Buchstaben: {some_char} und {another}')

    # Ermittle den Zeichencode für einen Buchstaben
    code = ord(some_char)      # = 108
    print (f'Zeichencode: {code}')

    # Ermittle den Buchstaben anhand des Zeichencodes
    code = 66
    char = chr(code)           # = 'B'
    print (f'Zeichen zum Code: {char}')

if __name__ == '__main__':
    main()