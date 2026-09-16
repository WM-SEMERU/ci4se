def guess_codec(file, errors='strict', require_char=False):
    gedcom_char_to_codec = {'ansel': 'gedcom'}
    bom_codec = check_bom(file)
    bom_size = file.tell()
    codec = bom_codec or 'gedcom'
    while True:
        line = file.readline()
        if not line:
            raise IOError('Unexpected EOF while reading GEDCOM header')
        line = line.lstrip().rstrip(b'\r\n')
        words = line.split()
        if len(words) >= 2 and words[0] == b'0' and words[1] != b'HEAD':
            if require_char:
                raise CodecError('GEDCOM header does not have CHAR record')
            else:
                break
        elif len(words) >= 3 and words[0] == b'1' and words[1] == b'CHAR':
            try:
                encoding = words[2].decode(codec, errors)
                encoding = gedcom_char_to_codec.get(encoding.lower(),
                    encoding.lower())
                new_codec = codecs.lookup(encoding).name
            except LookupError:
                raise CodecError('Unknown codec name {0}'.format(encoding))
            if bom_codec is None:
                codec = new_codec
            elif new_codec != bom_codec:
                raise CodecError(
                    'CHAR codec {0} is different from BOM codec {1}'.format
                    (new_codec, bom_codec))
            break
    return codec, bom_size