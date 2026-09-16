def decode_modified_utf8(data, errors='strict'):
    value, length = '', 0
    it = iter(decoder(data))
    while True:
        try:
            value += next(it)
            length += 1
        except StopIteration:
            break
        except UnicodeDecodeError as e:
            if errors == 'strict':
                raise e
            elif errors == 'ignore':
                pass
            elif errors == 'replace':
                value += '�'
                length += 1
    return value, length