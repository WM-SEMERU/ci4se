def create(self, basedir, outdir, name, prefix=None, dereference=True):
    basedir = ensure_text(basedir)
    tarpath = os.path.join(outdir, '{}.{}'.format(ensure_text(name), self.
        extension))
    with open_tar(tarpath, self.mode, dereference=dereference, errorlevel=1
        ) as tar:
        tar.add(basedir, arcname=prefix or '.')
    return tarpath