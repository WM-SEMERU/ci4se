def tempfile_writer(target):
    tmp = target.parent / ('_%s' % target.name)
    try:
        with tmp.open('wb') as fd:
            yield fd
    except:
        tmp.unlink()
        raise
    LOG.debug('rename %s -> %s', tmp, target)
    tmp.rename(target)