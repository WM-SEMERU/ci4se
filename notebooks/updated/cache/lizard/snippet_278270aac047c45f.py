def bban_base10(number):
    number = bban_compact(number)
    number = number[4:] + number[:4]
    return ''.join([str(IBAN_ALPHABET.index(char)) for char in number])