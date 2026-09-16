def _has_tag(version, debug=False):
    cmd = sh.git.bake('show-ref', '--verify', '--quiet', 'refs/tags/{}'.
        format(version))
    try:
        util.run_command(cmd, debug=debug)
        return True
    except sh.ErrorReturnCode:
        return False