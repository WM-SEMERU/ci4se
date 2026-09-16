def addgroupuser(username, uid, groupnames=None, system=False, no_login=
    True, no_password=False, gecos=None, sudo=False, **kwargs):
    group = addgroup(username, uid, system)
    user = adduser(username, uid, system, no_login, no_password, False,
        gecos, **kwargs)
    prefix = 'sudo ' if sudo else ''
    if groupnames:
        usermod = assignuser(username, groupnames)
        return '{0}{1} && {0}{2} && {0}{3}'.format(prefix, group, user, usermod
            )
    return '{0}{1} && {0}{2}'.format(prefix, group, user)