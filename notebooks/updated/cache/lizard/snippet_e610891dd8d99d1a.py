def bz2_opener(path, pattern='', verbose=False):
    source = path if is_url(path) else os.path.abspath(path)
    filename = os.path.basename(path)
    if pattern and not re.match(pattern, filename):
        logger.verbose('Skipping file: {}, did not match regex pattern "{}"'
            .format(os.path.abspath(path), pattern))
        return
    try:
        filehandle = bz2.open(io.BytesIO(urlopen(path).read())) if is_url(path
            ) else bz2.open(path)
        filehandle.read(1)
        filehandle.seek(0)
        logger.verbose('Processing file: {}'.format(source))
        yield filehandle
    except (OSError, IOError):
        raise BZ2ValidationError