def install(cert, password, keychain='/Library/Keychains/System.keychain',
    allow_any=False, keychain_password=None):
    if keychain_password is not None:
        unlock_keychain(keychain, keychain_password)
    cmd = 'security import {0} -P {1} -k {2}'.format(cert, password, keychain)
    if allow_any:
        cmd += ' -A'
    return __salt__['cmd.run'](cmd)