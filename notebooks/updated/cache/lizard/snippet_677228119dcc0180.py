def short_encode(input, errors='strict'):
    if not isinstance(input, text_type):
        input = text_type(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(short_table), length