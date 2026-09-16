def split(text):
    text = text.strip()
    text = re.sub('\\s+', ' ', text)
    space, quote, parts = ' ', '"', []
    part, quoted = '', False
    for char in text:
        if char is quote and quoted is False:
            quoted = True
            continue
        if char is quote and quoted is True:
            quoted = False
            parts.append(part.strip())
            part = ''
            continue
        if char is space and quoted is True:
            part += char
            continue
        if char is space:
            if part:
                parts.append(part)
                part = ''
            continue
        if char is not space:
            part += char
            continue
    if part:
        parts.append(part.strip())
    return parts