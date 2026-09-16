def wrap(item, args=None, krgs=None, **kwargs):
    with Wrap(**kwargs):
        if callable(item):
            args = args or []
            krgs = krgs or {}
            item(*args, **krgs)
        else:
            echo(item)