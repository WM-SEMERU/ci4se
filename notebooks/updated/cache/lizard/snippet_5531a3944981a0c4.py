def dev_tools_installer(cv, ctx, site):
    log = logging.getLogger('ipsv.installer.dev_tools')
    log.info('Loading installer for Dev Tools %s', cv)
    iv = None
    for v in versions:
        vstring = '.'.join(map(str, v)) if v else 'latest'
        log.debug('Checking if version %s >= %s', vstring, cv.vstring)
        if v is None or v >= cv:
            log.debug('Changing installer version to %s', vstring)
            iv = v
    log.info('Returning installer version %s', '.'.join(map(str, iv)) if iv
         else 'latest')
    return versions[iv](ctx, site)