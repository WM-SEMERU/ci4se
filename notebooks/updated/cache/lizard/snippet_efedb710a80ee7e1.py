def strip_accents(text):
    normalized_str = unicodedata.normalize('NFD', text)
    return ''.join([c for c in normalized_str if unicodedata.category(c) !=
        'Mn'])