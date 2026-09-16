def exec_action(module, action, module_parameter=None, action_parameter=
    None, state_only=False):
    out = __salt__['cmd.run']('eselect --brief --colour=no {0} {1} {2} {3}'
        .format(module, module_parameter or '', action, action_parameter or
        ''), python_shell=False)
    out = out.strip().split('\n')
    if out[0].startswith('!!! Error'):
        return False
    if state_only:
        return True
    if not out:
        return False
    if len(out) == 1 and not out[0].strip():
        return False
    return out