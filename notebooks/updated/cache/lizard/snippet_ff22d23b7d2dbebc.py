def write_file(path, content, mode=None, encoding='utf-8'):
    if not mode:
        if isinstance(content, bytes):
            mode = 'wb'
        else:
            mode = 'wt'
    if not path:
        raise ValueError('Output path is invalid')
    else:
        getLogger().debug('Writing content to {}'.format(path))
        if mode in ('w', 'wt') and not isinstance(content, str):
            content = to_string(content)
        elif mode == 'wb':
            if not isinstance(content, str):
                content = to_string(content).encode(encoding)
            else:
                content = content.encode(encoding)
        if str(path).endswith('.gz'):
            with gzip.open(path, mode) as outfile:
                outfile.write(content)
        else:
            with open(path, mode=mode) as outfile:
                outfile.write(content)