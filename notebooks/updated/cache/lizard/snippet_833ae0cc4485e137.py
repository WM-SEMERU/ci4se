def tee_output_python():
    buffer = StringIO()
    out = CapturedStdout(buffer)
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    flush()
    sys.stdout = TeeingStreamProxy(sys.stdout, buffer)
    sys.stderr = TeeingStreamProxy(sys.stderr, buffer)
    try:
        yield out
    finally:
        flush()
        out.finalize()
        sys.stdout, sys.stderr = orig_stdout, orig_stderr