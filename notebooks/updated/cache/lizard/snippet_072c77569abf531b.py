def _write_json(filepath, data, kwargs):
    with io_stl.open(filepath, 'w', encoding='utf8') as outfile:
        if 'indent' not in kwargs:
            kwargs['indent'] = 4
        if 'sort_keys' not in kwargs:
            kwargs['sort_keys'] = True
        if 'separators' not in kwargs:
            kwargs['separators'] = ',', ': '
        if 'ensure_ascii' not in kwargs:
            kwargs['ensure_ascii'] = False
        str_ = json.dumps(data, **kwargs)
        outfile.write(to_unicode(str_))
    return data