def get_proc_name(cmd):
    if isinstance(cmd, Iterable) and not isinstance(cmd, str):
        cmd = ' '.join(cmd)
    return cmd.split()[0].replace('(', '').replace(')', '')