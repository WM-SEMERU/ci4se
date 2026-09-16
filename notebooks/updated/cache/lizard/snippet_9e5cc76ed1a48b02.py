def which_bin(exes):

    def wrapper(function):

        def wrapped(*args, **kwargs):
            if salt.utils.path.which_bin(exes) is None:
                raise CommandNotFoundError(
                    'None of provided binaries({0}) was not found in $PATH.'
                    .format(["'{0}'".format(exe) for exe in exes]))
            return function(*args, **kwargs)
        return identical_signature_wrapper(function, wrapped)
    return wrapper