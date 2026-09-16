def is_installed(pkgname=None, bin_env=None, user=None, cwd=None):
    for line in freeze(bin_env=bin_env, user=user, cwd=cwd):
        if line.startswith('-f') or line.startswith('#'):
            continue
        elif line.startswith('-e hg+not trust'):
            continue
        elif line.startswith('-e'):
            line = line.split('-e ')[1]
            version_, name = line.split('#egg=')
        elif len(line.split('===')) >= 2:
            name = line.split('===')[0]
            version_ = line.split('===')[1]
        elif len(line.split('==')) >= 2:
            name = line.split('==')[0]
            version_ = line.split('==')[1]
        else:
            logger.error("Can't parse line '%s'", line)
            continue
        if pkgname:
            if pkgname == name.lower():
                return True
    return False