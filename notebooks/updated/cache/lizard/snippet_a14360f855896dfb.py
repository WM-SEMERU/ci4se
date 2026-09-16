def verify(path):
    valid = False
    try:
        zf = zipfile.ZipFile(path)
    except (zipfile.BadZipfile, IsADirectoryError):
        pass
    else:
        names = sorted(zf.namelist())
        names = [nn for nn in names if nn.endswith('.tif')]
        names = [nn for nn in names if nn.startswith('SID PHA')]
        for name in names:
            with zf.open(name) as pt:
                fd = io.BytesIO(pt.read())
                if SingleTifPhasics.verify(fd):
                    valid = True
                    break
        zf.close()
    return valid