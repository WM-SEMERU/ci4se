def deaccent(text):
    norm = unicodedata.normalize('NFD', text)
    result = ''.join(ch for ch in norm if unicodedata.category(ch) != 'Mn')
    return unicodedata.normalize('NFC', result)