def check_output(*args, **kwargs):
    if hasattr(subprocess, 'check_output'):
        return subprocess.check_output(*args, stderr=subprocess.STDOUT,
            universal_newlines=True, **kwargs)
    else:
        process = subprocess.Popen(*args, stdout=subprocess.PIPE, stderr=
            subprocess.STDOUT, universal_newlines=True, **kwargs)
        output, _ = process.communicate()
        retcode = process.poll()
        if retcode:
            error = subprocess.CalledProcessError(retcode, args[0])
            error.output = output
            raise error
        return output