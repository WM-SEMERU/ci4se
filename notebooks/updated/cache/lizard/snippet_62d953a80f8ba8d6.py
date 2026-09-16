def chmod_native(path, mode_expression, recursive=False):
    popenargs = ['chmod']
    if recursive:
        popenargs.append('-R')
    popenargs.append(mode_expression)
    popenargs.append(path)
    subprocess.check_call(popenargs)