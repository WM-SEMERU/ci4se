def replace(text):
    for hex, value in UNICODE_DICTIONARY.items():
        num = int(hex[3:-1], 16)
        decimal = '&#' + str(num) + ';'
        for key in [hex, decimal]:
            text = text.replace(key, value)
    return text