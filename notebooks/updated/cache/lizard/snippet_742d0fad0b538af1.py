def expand_braces(patterns, flags):
    if flags & BRACE:
        for p in ([patterns] if isinstance(patterns, (str, bytes)) else
            patterns):
            try:
                yield from bracex.iexpand(p, keep_escapes=True)
            except Exception:
                yield p
    else:
        for p in ([patterns] if isinstance(patterns, (str, bytes)) else
            patterns):
            yield p