def smart_open(filename: str, mode: str='rt', ftype: str='auto', errors:
    str='replace'):
    if ftype in ('gzip', 'gz') or ftype == 'auto' and filename.endswith('.gz'
        ) or ftype == 'auto' and 'r' in mode and is_gzip_file(filename):
        return gzip.open(filename, mode=mode, encoding='utf-8', errors=errors)
    else:
        return open(filename, mode=mode, encoding='utf-8', errors=errors)