def convert_to_ascii(statement):
    import unicodedata
    text = unicodedata.normalize('NFKD', statement.text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    statement.text = str(text)
    return statement