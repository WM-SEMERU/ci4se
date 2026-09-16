def copy_tree(src, dst, symlinks=False, ignore=[]):
    names = os.listdir(src)
    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignore:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copy_tree(srcname, dstname, symlinks, ignore)
            else:
                copy_file(srcname, dstname)
        except (IOError, os.error) as exc:
            errors.append((srcname, dstname, str(exc)))
        except CTError as exc:
            errors.extend(exc.errors)
    if errors:
        raise CTError(errors)