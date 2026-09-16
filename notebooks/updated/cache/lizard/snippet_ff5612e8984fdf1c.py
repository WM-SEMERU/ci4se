def tag(check, version, push, dry_run):
    tagging_all = check == 'all'
    valid_checks = get_valid_checks()
    if not tagging_all and check not in valid_checks:
        abort('Check `{}` is not an Agent-based Integration'.format(check))
    if tagging_all:
        if version:
            abort('You cannot tag every check with the same version')
        checks = sorted(valid_checks)
    else:
        checks = [check]
    tagged = False
    for check in checks:
        echo_info('{}:'.format(check))
        if not version:
            version = get_version_string(check)
        release_tag = get_release_tag_string(check, version)
        echo_waiting('Tagging HEAD with {}... '.format(release_tag), indent
            =True, nl=False)
        if dry_run:
            version = None
            click.echo()
            continue
        result = git_tag(release_tag, push)
        if result.code == 128 or 'already exists' in result.stderr:
            echo_warning('already exists')
        elif result.code != 0:
            abort('\n{}{}'.format(result.stdout, result.stderr), code=
                result.code)
        else:
            tagged = True
            echo_success('success!')
        version = None
    if not tagged:
        abort(code=2)