def write_json(data, filename, gzip_mode=False):
    open_file = open
    if gzip_mode:
        open_file = gzip.open
    try:
        with open_file(filename, 'wt') as fh:
            json.dump(obj=data, fp=fh, sort_keys=True)
    except AttributeError:
        fh = open_file(filename, 'wt')
        json.dump(obj=data, fp=fh, sort_keys=True)
        fh.close()