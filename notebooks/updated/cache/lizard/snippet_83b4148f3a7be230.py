def install_package(package, wheels_path, venv=None, requirement_files=None,
    upgrade=False, install_args=None):
    requirement_files = requirement_files or []
    logger.info('Installing %s...', package)
    if venv and not os.path.isdir(venv):
        raise WagonError('virtualenv {0} does not exist'.format(venv))
    pip_command = _construct_pip_command(package, wheels_path, venv,
        requirement_files, upgrade, install_args)
    if IS_VIRTUALENV and not venv:
        logger.info('Installing within current virtualenv')
    result = _run(pip_command)
    if not result.returncode == 0:
        raise WagonError('Could not install package: {0} ({1})'.format(
            package, result.aggr_stderr))