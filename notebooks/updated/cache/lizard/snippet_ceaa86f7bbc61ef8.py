def escape_string(text):
    if text is None:
        return text
    TO_REMOVE = ['&', '%', '$', '#', '_', '{', '}', '~', '^', '\\\\']
    for char in TO_REMOVE:
        text = text.replace(char, '')
    return text