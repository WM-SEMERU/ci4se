def loads(s, **kwargs):
    try:
        return _engine[0](s)
    except _engine[2]:
        why = sys.exc_info()[1]
        raise JSONError(why)