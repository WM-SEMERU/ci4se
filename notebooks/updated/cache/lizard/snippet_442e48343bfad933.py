def group_to_gid(group):
    func_name = '{0}.group_to_gid'.format(__virtualname__)
    if __opts__.get('fun', '') == func_name:
        log.info(
            'The function %s should not be used on Windows systems; see function docs for details.'
            , func_name)
    if group is None:
        return ''
    return salt.utils.win_dacl.get_sid_string(group)