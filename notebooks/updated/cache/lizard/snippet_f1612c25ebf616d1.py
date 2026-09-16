def from_file(cls, fp, format_=None, fps=None, **kwargs):
    if format_ is None:
        text = fp.read()
        fragment = text[:10000]
        format_ = autodetect_format(fragment)
        fp = io.StringIO(text)
    impl = get_format_class(format_)
    subs = cls()
    subs.format = format_
    subs.fps = fps
    impl.from_file(subs, fp, format_, fps=fps, **kwargs)
    return subs