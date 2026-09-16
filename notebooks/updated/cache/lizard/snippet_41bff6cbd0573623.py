def untar(tarpath, outfolder, owners=None, overwrite=True, fixperms=True):
    _ignored = fixperms
    with tmpdir():
        _, _, ext = tarpath.rpartition('.')
        if ext not in ('gz', 'bz2', 'xz'):
            raise ValueError('tarpath must point to a .gz, .bz2, or .xz file')
        tf = tarfile.open(tarpath, 'r:' + ext)
        try:
            os.mkdir('contents')
            tf.extractall('contents')
        finally:
            tf.close()
        if owners is not None:
            contents = path.Path('contents')
            for item in contents.walk():
                if item.isdir():
                    item.chown(*owners)
                    item.chmod('ug+xr')
                if item.isfile() and not item.islink():
                    item.chown(*owners)
                    item.chmod('ug+rw')
        if os.path.isdir(outfolder):
            if overwrite:
                shutil.rmtree(outfolder)
            else:
                raise IOError(
                    'Cannot untar %s because %s already exists and overwrite=False'
                     % (tarfile, outfolder))
        shutil.move('contents', outfolder)