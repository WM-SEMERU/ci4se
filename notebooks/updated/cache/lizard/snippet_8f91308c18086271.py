def get_text_v4(address, stream, mapped=False):
    if address == 0:
        return ''
    if mapped:
        size, _ = TWO_UINT64_uf(stream, address + 8)
        text_bytes = stream[address + 24:address + size]
    else:
        stream.seek(address + 8)
        size, _ = TWO_UINT64_u(stream.read(16))
        text_bytes = stream.read(size - 24)
    try:
        text = text_bytes.strip(b' \r\t\n\x00').decode('utf-8')
    except UnicodeDecodeError as err:
        try:
            from cchardet import detect
            encoding = detect(text_bytes)['encoding']
            text = text_bytes.decode(encoding).strip(' \r\t\n\x00')
        except ImportError:
            logger.warning(
                'Unicode exception occured and "cChardet" package is not installed. Mdf version 4 expects "utf-8" strings and this package may detect if a different encoding was used'
                )
            raise err
    return text