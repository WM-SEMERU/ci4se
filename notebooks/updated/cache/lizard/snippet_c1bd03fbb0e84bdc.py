def ziparchive_opener(path, pattern='', verbose=False):
    with (zipfile.ZipFile(io.BytesIO(urlopen(path).read()), 'r') if is_url(
        path) else zipfile.ZipFile(path, 'r')) as ziparchive:
        for zipinfo in ziparchive.infolist():
            if not zipinfo.filename.endswith('/'):
                source = os.path.join(path, zipinfo.filename)
                if pattern and not re.match(pattern, zipinfo.filename):
                    logger.verbose(
                        'Skipping file: {}, did not match regex pattern "{}"'
                        .format(os.path.abspath(zipinfo.filename), pattern))
                    continue
                logger.verbose('Processing file: {}'.format(source))
                filehandle = ziparchive.open(zipinfo)
                yield filehandle