def main(argd):
    startdir = argd['DIR'] or '/'
    if not os.path.isdir(startdir):
        raise InvalidArg('not a valid start directory: {}'.format(startdir))
    if argd['--progress']:
        return walk_dir_progress(startdir)
    return walk_dir_animated(startdir)