def save_image(byteio, imgfmt):
    from os import path, mkdir
    ptdir = '{}.{}'.format(project, task)
    uuid = str(uuid4())
    idir = path.join(dbdir, ptdir)
    if not path.isdir(idir):
        mkdir(idir)
    ipath = path.join(idir, '{}.{}'.format(uuid, imgfmt))
    with open(ipath, 'wb') as f:
        f.write(byteio)
    return uuid