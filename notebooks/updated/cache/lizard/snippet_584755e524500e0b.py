def die(fmt, *args):
    if not len(args):
        raise SystemExit('error: ' + text_type(fmt))
    raise SystemExit('error: ' + fmt % args)