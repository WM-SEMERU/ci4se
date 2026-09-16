def disable_stdout_buffering():
    stdout_orig = sys.stdout
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    return stdout_orig