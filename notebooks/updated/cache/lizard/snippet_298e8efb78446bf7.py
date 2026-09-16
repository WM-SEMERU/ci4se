def readable_popen(*args, **kwargs):
    kwargs['stdout'] = subprocess.PIPE
    kwargs['stderr'] = subprocess.STDOUT
    p = subprocess.Popen(*args, **kwargs)
    for line in iter(lambda : p.stdout.readline(), ''):
        if six.PY3:
            line = line.decode('utf-8')
        yield line.rstrip()
    p.communicate()
    yield p