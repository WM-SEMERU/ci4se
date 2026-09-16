def checkIfRemoteIsNewer(self, localfile):
    is_remote_newer = False
    if localfile.exists() and localfile.stat().st_size > 0:
        LOG.info('File exists locally, using cache')
    else:
        is_remote_newer = True
        LOG.info('No cache file, fetching entries')
    return is_remote_newer