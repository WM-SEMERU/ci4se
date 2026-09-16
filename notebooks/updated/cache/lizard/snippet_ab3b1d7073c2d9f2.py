def shortened(text, size=120):
    if text:
        text = text.strip()
        if len(text) > size:
            return '%s...' % text[:size - 3].strip()
    return text