def _run_cmd(cmd, ctx, glob, loc):
    if PDB:
        _enable_pdb()
    if IPYTHON:
        from IPython import start_ipython
        args_ipy = ['-i', '--gui=qt']
        ns = glob.copy()
        ns.update(loc)
        return start_ipython(args_ipy, user_ns=ns)
    prof = __builtins__.get('profile', None)
    if prof:
        prof = __builtins__['profile']
        return _profile(prof, cmd, glob, loc)
    return exec_(cmd, glob, loc)