def determine_encoding(path, default=None):
    byte_order_marks = ('utf-8-sig', (codecs.BOM_UTF8,)), ('utf-16', (
        codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)), ('utf-32', (codecs.
        BOM_UTF32_LE, codecs.BOM_UTF32_BE))
    try:
        with open(path, 'rb') as infile:
            raw = infile.read(4)
    except IOError:
        return default
    for encoding, boms in byte_order_marks:
        if any(raw.startswith(bom) for bom in boms):
            return encoding
    return default