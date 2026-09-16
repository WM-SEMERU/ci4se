def decode(ew):
    _, charset, cte, cte_string, _ = str(ew).split('?')
    charset, _, lang = charset.partition('*')
    cte = cte.lower()
    bstring = cte_string.encode('ascii', 'surrogateescape')
    bstring, defects = _cte_decoders[cte](bstring)
    try:
        string = bstring.decode(charset)
    except UnicodeError:
        defects.append(errors.UndecodableBytesDefect(
            'Encoded word contains bytes not decodable using {} charset'.
            format(charset)))
        string = bstring.decode(charset, 'surrogateescape')
    except LookupError:
        string = bstring.decode('ascii', 'surrogateescape')
        if charset.lower() != 'unknown-8bit':
            defects.append(errors.CharsetError(
                'Unknown charset {} in encoded word; decoded as unknown bytes'
                .format(charset)))
    return string, charset, lang, defects