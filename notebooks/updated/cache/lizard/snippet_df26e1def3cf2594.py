def drop_bad_characters(text):
    text = ''.join([c for c in text if c in ALLOWED_CHARS])
    return text