def importFile(self, path, mode, outp=None):
    if not os.path.isfile(path):
        raise s_exc.NoSuchFile('File does not exist')
    fname = os.path.split(path)[1]
    parts = fname.rsplit('.', 1)
    ext = parts[1] if len(parts) is 2 else None
    if not ext or ext not in ('crt', 'key', 'p12'):
        mesg = 'importFile only supports .crt, .key, .p12 extensions'
        raise s_exc.BadFileExt(mesg=mesg, ext=ext)
    newpath = s_common.genpath(self.certdir, mode, fname)
    if os.path.isfile(newpath):
        raise s_exc.FileExists('File already exists')
    shutil.copy(path, newpath)
    if outp is not None:
        outp.printf('copied %s to %s' % (path, newpath))