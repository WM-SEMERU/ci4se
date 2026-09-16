def sys_maxfd():
    maxfd = None
    try:
        maxfd = int(resource.getrlimit(resource.RLIMIT_NOFILE)[0])
        if maxfd == resource.RLIM_INFINITY:
            maxfd = None
    except:
        pass
    if maxfd is None:
        maxfd = sys_maxfd.fallback_maxfd
    return maxfd