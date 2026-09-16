def _lfs_add(files, git):
    larges, huges = [], []
    for file in files:
        size = os.path.getsize(file)
        if size > 100 * 1024 * 1024:
            larges.append(file)
        elif size > 2 * 1024 * 1024 * 1024:
            huges.append(file)
    if huges:
        raise Error(_(
            """These files are too large to be submitted:
{}
Remove these files from your directory and then re-run {}!"""
            ).format('\n'.join(huges), org))
    if larges:
        if not shutil.which('git-lfs'):
            raise Error(_(
                """These files are too large to be submitted:
{}
Install git-lfs (or remove these files from your directory) and then re-run!"""
                ).format('\n'.join(larges)))
        _run(git('lfs install --local'))
        _run(git('config credential.helper cache'))
        for large in larges:
            _run(git('rm --cached {}'.format(shlex.quote(large))))
            _run(git('lfs track {}'.format(shlex.quote(large))))
            _run(git('add {}'.format(shlex.quote(large))))
        _run(git('add --force .gitattributes'))