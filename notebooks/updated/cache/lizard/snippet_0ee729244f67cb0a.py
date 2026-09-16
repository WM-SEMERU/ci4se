def is_ansi_capable():
    BUILD_ANSI_AVAIL = 10586
    CURRENT_VERS = sys.getwindowsversion()[:3]
    if CURRENT_VERS[2] > BUILD_ANSI_AVAIL:
        result = True
    else:
        result = False
    log.debug('version %s %s', CURRENT_VERS, result)
    return result