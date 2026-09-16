def find_pip(pip_version=None, python_version=None):
    pip_exe = 'pip'
    try:
        context = create_context(pip_version, python_version)
    except BuildError as e:
        from rez.backport.shutilwhich import which
        pip_exe = which('pip')
        if pip_exe:
            print_warning(
                "pip rez package could not be found; system 'pip' command (%s) will be used instead."
                 % pip_exe)
            context = None
        else:
            raise e
    return pip_exe, context