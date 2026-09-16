def mkdir(path, create_parent=True, check_if_exists=False):
    cmd = _format_cmd('mkdir', path, _p=create_parent)
    if check_if_exists:
        return 'if [[ ! -d {0} ]]; then {1}; fi'.format(path, cmd)
    return cmd