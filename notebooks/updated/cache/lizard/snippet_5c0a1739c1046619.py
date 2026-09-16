def platform_detect():
    pi = pi_version()
    if pi is not None:
        return RASPBERRY_PI
    plat = platform.platform()
    if plat.lower().find('armv7l-with-debian') > -1:
        return BEAGLEBONE_BLACK
    elif plat.lower().find('armv7l-with-ubuntu') > -1:
        return BEAGLEBONE_BLACK
    elif plat.lower().find('armv7l-with-glibc2.4') > -1:
        return BEAGLEBONE_BLACK
    elif plat.lower().find('armv7l-with-arch') > -1:
        return BEAGLEBONE_BLACK
    return UNKNOWN