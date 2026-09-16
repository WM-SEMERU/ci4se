def serialize(element, strip=False):
    text = etree.tostring(element, method='text', encoding='utf-8')
    if strip:
        text = text.strip()
    return str(text, encoding='utf-8')