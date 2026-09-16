def _set_shortcut_ownership(path, user):
    try:
        __salt__['file.lchown'](path, user)
    except OSError:
        pass
    return _check_shortcut_ownership(path, user)