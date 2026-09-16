def dumps(props, separator='=', comments=None, timestamp=True, sort_keys=False
    ):
    s = StringIO()
    dump(props, s, separator=separator, comments=comments, timestamp=
        timestamp, sort_keys=sort_keys)
    return s.getvalue()