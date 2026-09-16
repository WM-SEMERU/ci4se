def tararchive_opener(path, pattern='', verbose=False):
    with (tarfile.open(fileobj=io.BytesIO(urlopen(path).read())) if is_url(
        path) else tarfile.open(path)) as tararchive:
        for tarinfo in tararchive:
            if tarinfo.isfile():
                source = os.path.join(path, tarinfo.name)
                if pattern and not re.match(pattern, tarinfo.name):
                    logger.verbose(
                        'Skipping file: {}, did not match regex pattern "{}"'
                        .format(os.path.abspath(tarinfo.name), pattern))
                    continue
                logger.verbose('Processing file: {}'.format(source))
                filehandle = tararchive.extractfile(tarinfo)
                yield filehandle