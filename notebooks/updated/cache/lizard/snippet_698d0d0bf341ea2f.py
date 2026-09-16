def ignore_broken_pipe():
    for f in (sys.stdin, sys.stdout, sys.stderr):
        try:
            f.close()
        except BrokenPipeError:
            pass