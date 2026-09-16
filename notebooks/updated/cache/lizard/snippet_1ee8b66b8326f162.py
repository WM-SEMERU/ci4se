def _do_shell(self, line):
    if not line:
        return
    sp = Popen(line, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
        close_fds=not WINDOWS)
    fo, fe = sp.stdout, sp.stderr
    if PY2:
        out = fo.read().strip(EOL)
        err = fe.read().strip(EOL)
    else:
        out = fo.read().decode('utf-8')
        err = fe.read().decode('utf-8')
    if out:
        print(out)
        return
    if err:
        print(err.replace('isbn_', ''))