def decode_html(html):
    if isinstance(html, unicode):
        return html
    match = CHARSET_META_TAG_PATTERN.search(html)
    if match:
        declared_encoding = match.group(1).decode('ASCII')
        with ignored(LookupError):
            return html.decode(declared_encoding, 'ignore')
    with ignored(UnicodeDecodeError):
        return html.decode('utf8')
    text = TAG_MARK_PATTERN.sub(to_bytes(' '), html)
    diff = text.decode('utf8', 'ignore').encode('utf8')
    sizes = len(diff), len(text)
    if abs(len(text) - len(diff)) < max(sizes) * 0.01:
        return html.decode('utf8', 'ignore')
    encoding = 'utf8'
    encoding_detector = chardet.detect(text)
    if encoding_detector['encoding']:
        encoding = encoding_detector['encoding']
    return html.decode(encoding, 'ignore')