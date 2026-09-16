def read_clipboard(sep='\\s+', **kwargs):
    r
    encoding = kwargs.pop('encoding', 'utf-8')
    if encoding is not None and encoding.lower().replace('-', '') != 'utf8':
        raise NotImplementedError(
            'reading from clipboard only supports utf-8 encoding')
    from pandas.io.clipboard import clipboard_get
    from pandas.io.parsers import read_csv
    text = clipboard_get()
    try:
        text = text.decode(kwargs.get('encoding') or get_option(
            'display.encoding'))
    except AttributeError:
        pass
    lines = text[:10000].split('\n')[:-1][:10]
    counts = {x.lstrip().count('\t') for x in lines}
    if len(lines) > 1 and len(counts) == 1 and counts.pop() != 0:
        sep = '\t'
    if sep is None and kwargs.get('delim_whitespace') is None:
        sep = '\\s+'
    if len(sep) > 1 and kwargs.get('engine') is None:
        kwargs['engine'] = 'python'
    elif len(sep) > 1 and kwargs.get('engine') == 'c':
        warnings.warn(
            'read_clipboard with regex separator does not work properly with c engine'
            )
    return read_csv(StringIO(text), sep=sep, **kwargs)