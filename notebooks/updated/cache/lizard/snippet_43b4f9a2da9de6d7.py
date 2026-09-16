def humanize_bytes(bytes, precision=1):
    abbrevs = (1 << 50, 'PB'), (1 << 40, 'TB'), (1 << 30, 'GB'), (1 << 20, 'MB'
        ), (1 << 10, 'kB'), (1, 'bytes')
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)