def to_unicode(string):
    if not is_unicode(string):
        for codec in CODECS:
            try:
                unic = to_text_string(string, codec)
            except UnicodeError:
                pass
            except TypeError:
                break
            else:
                return unic
    return string