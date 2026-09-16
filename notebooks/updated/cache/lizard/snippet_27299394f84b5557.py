def _check_valid_version():
    bower_version = _LooseVersion(__salt__['cmd.run']('bower --version'))
    valid_version = _LooseVersion('1.3')
    if bower_version < valid_version:
        raise CommandExecutionError(
            "'bower' is not recent enough({0} < {1}). Please Upgrade.".
            format(bower_version, valid_version))