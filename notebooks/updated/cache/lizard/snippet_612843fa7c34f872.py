def _check_and_install_ruby(ret, ruby, default=False, user=None):
    ret = _ruby_installed(ret, ruby, user=user)
    if not ret['result']:
        if __salt__['rbenv.install_ruby'](ruby, runas=user):
            ret['result'] = True
            ret['changes'][ruby] = 'Installed'
            ret['comment'] = 'Successfully installed ruby'
            ret['default'] = default
        else:
            ret['result'] = False
            ret['comment'] = 'Failed to install ruby'
            return ret
    if default:
        __salt__['rbenv.default'](ruby, runas=user)
    return ret