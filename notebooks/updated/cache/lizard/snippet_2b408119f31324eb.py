def upload(ctx, check, sdist, dry_run):
    if check in get_valid_checks():
        check_dir = os.path.join(get_root(), check)
    else:
        check_dir = resolve_path(check)
        if not dir_exists(check_dir):
            abort('`{}` is not an Agent-based Integration or Python package'
                .format(check))
        check = basepath(check_dir)
    pypi_config = ctx.obj.get('pypi', {})
    username = pypi_config.get('user') or os.getenv('TWINE_USERNAME')
    password = pypi_config.get('pass') or os.getenv('TWINE_PASSWORD')
    if not (username and password):
        abort(
            'This requires pypi.user and pypi.pass configuration. Please see `ddev config -h`.'
            )
    auth_env_vars = {'TWINE_USERNAME': username, 'TWINE_PASSWORD': password}
    echo_waiting('Building and publishing `{}` to PyPI...'.format(check))
    with chdir(check_dir, env_vars=auth_env_vars):
        result = build_package(check_dir, sdist)
        if result.code != 0:
            abort(result.stdout, result.code)
        echo_waiting('Uploading the package...')
        if not dry_run:
            result = run_command('twine upload --skip-existing dist{}*'.
                format(os.path.sep))
            if result.code != 0:
                abort(code=result.code)
    echo_success('Success!')