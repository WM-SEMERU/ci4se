def unzip(filename, match_dir=False, destdir=None):
    if not destdir:
        destdir = '.'
    z = zipfile.ZipFile(filename)
    unzipped = '.'
    if match_dir:
        if not filename.endswith('.zip'):
            raise FileException('Expected .zip file extension', filename)
        unzipped = os.path.basename(filename)[:-4]
        check_extracted_paths(z.namelist(), unzipped)
    else:
        check_extracted_paths(z.namelist())
    for info in z.infolist():
        log.debug('Extracting %s to %s', info.filename, destdir)
        z.extract(info, destdir)
        perms = info.external_attr >> 16 & 4095
        if perms > 0:
            os.chmod(os.path.join(destdir, info.filename), perms)
    return os.path.join(destdir, unzipped)