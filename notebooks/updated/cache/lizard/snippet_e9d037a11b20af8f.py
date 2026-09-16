def popen_wrapper(args):
    try:
        p = Popen(args, shell=False, stdout=PIPE, stderr=PIPE, close_fds=os
            .name != 'nt', universal_newlines=True)
    except OSError as e:
        raise OSError("Error executing '{:}': '{:}'".format(args[0], e.
            strerror))
    output, errors = p.communicate()
    return output, text_type(errors), p.returncode