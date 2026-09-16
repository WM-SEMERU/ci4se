def has_privileged_access(executable):
    if sys.platform.startswith('win'):
        return True
    if sys.platform.startswith('darwin'):
        if os.stat(executable).st_uid == 0:
            return True
    if os.geteuid() == 0:
        return True
    if os.stat(executable).st_uid == 0 and (os.stat(executable).st_mode &
        stat.S_ISUID or os.stat(executable).st_mode & stat.S_ISGID):
        return True
    try:
        if sys.platform.startswith('linux'
            ) and 'security.capability' in os.listxattr(executable):
            caps = os.getxattr(executable, 'security.capability')
            if struct.unpack('<IIIII', caps)[1] & 1 << 13:
                return True
    except (AttributeError, OSError) as e:
        log.error(
            'could not determine if CAP_NET_RAW capability is set for {}: {}'
            .format(executable, e))
    return False