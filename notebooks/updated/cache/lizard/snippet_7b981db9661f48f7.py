def utf(text):
    try:
        output = unicode(text, encoding='utf-8')
    except UnicodeDecodeError:
        output = text
    except TypeError:
        output = text
    return output