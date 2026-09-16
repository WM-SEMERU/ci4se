def compile_file(self, filepath, write=True, package=False, *args, **kwargs):
    set_ext = False
    if write is False:
        destpath = None
    elif write is True:
        destpath = filepath
        set_ext = True
    elif os.path.splitext(write)[1]:
        destpath = write
    else:
        destpath = os.path.join(write, os.path.basename(filepath))
        set_ext = True
    if set_ext:
        base, ext = os.path.splitext(os.path.splitext(destpath)[0])
        if not ext:
            ext = comp_ext
        destpath = fixpath(base + ext)
    if filepath == destpath:
        raise CoconutException('cannot compile ' + showpath(filepath) +
            ' to itself', extra='incorrect file extension')
    self.compile(filepath, destpath, package, *args, **kwargs)
    return destpath