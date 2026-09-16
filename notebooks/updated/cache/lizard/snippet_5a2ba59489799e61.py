def get_version(with_git_hash=True, refresh_hash=False):
    version = __version__
    if with_git_hash:
        global INDRA_GITHASH
        if INDRA_GITHASH is None or refresh_hash:
            with open(devnull, 'w') as nul:
                try:
                    ret = check_output(['git', 'rev-parse', 'HEAD'], cwd=
                        dirname(__file__), stderr=nul)
                except CalledProcessError:
                    ret = 'UNHASHED'
            INDRA_GITHASH = ret.strip().decode('utf-8')
        version = '%s-%s' % (version, INDRA_GITHASH)
    return version