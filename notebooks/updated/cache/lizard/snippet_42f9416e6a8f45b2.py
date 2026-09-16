def recursive_overwrite(src, dest, ignore=None):
    if os.path.islink(src):
        linkto = os.readlink(src)
        if os.path.exists(dest):
            os.remove(dest)
        symlink(linkto, dest)
    elif os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for _ in files:
            if _ not in ignored:
                recursive_overwrite(os.path.join(src, _), os.path.join(dest,
                    _), ignore)
    else:
        shutil.copyfile(src, dest)