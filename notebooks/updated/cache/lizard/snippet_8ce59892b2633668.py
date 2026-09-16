def _extract_member(self, member, targetpath, pwd):
    if targetpath[-1:] in (os.path.sep, os.path.altsep) and len(os.path.
        splitdrive(targetpath)[1]) > 1:
        targetpath = targetpath[:-1]
    if member.filename[0] == '/':
        targetpath = os.path.join(targetpath, member.filename[1:])
    else:
        targetpath = os.path.join(targetpath, member.filename)
    targetpath = os.path.normpath(targetpath)
    upperdirs = os.path.dirname(targetpath)
    if upperdirs and not os.path.exists(upperdirs):
        os.makedirs(upperdirs)
    if member.filename[-1] == '/':
        if not os.path.isdir(targetpath):
            os.mkdir(targetpath)
        return targetpath
    source = self.open(member, pwd=pwd)
    target = file(targetpath, 'wb')
    shutil.copyfileobj(source, target)
    source.close()
    target.close()
    return targetpath