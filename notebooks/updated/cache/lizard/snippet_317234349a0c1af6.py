def call(args, stdout=PIPE, stderr=PIPE):
    p = Popen(args, stdout=stdout, stderr=stderr)
    out, err = p.communicate()
    try:
        return out.decode(sys.stdout.encoding), err.decode(sys.stdout.encoding)
    except Exception:
        return out, err