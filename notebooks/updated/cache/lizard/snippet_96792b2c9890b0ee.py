def _create_pbuilders(env, runas='root'):
    home = os.path.expanduser('~{0}'.format(runas))
    pbuilderrc = os.path.join(home, '.pbuilderrc')
    if not os.path.isfile(pbuilderrc):
        raise SaltInvocationError('pbuilderrc environment is incorrectly setup'
            )
    env_overrides = _get_build_env(env)
    if env_overrides and not env_overrides.isspace():
        with salt.utils.files.fopen(pbuilderrc, 'a') as fow:
            fow.write(salt.utils.stringutils.to_str(env_overrides))
    cmd = 'chown {0}:{0} {1}'.format(runas, pbuilderrc)
    retrc = __salt__['cmd.retcode'](cmd, runas='root')
    if retrc != 0:
        raise SaltInvocationError(
            "Create pbuilderrc in home directory failed with return error '{0}', check logs for further details"
            .format(retrc))