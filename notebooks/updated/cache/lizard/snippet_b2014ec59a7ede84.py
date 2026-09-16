def _mergetree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            log.info('Copying folder %s to %s', s, d)
            if os.path.exists(d):
                _mergetree(s, d)
            else:
                shutil.copytree(s, d)
        else:
            log.info('Copying file %s to %s', s, d)
            shutil.copy2(s, d)