def _strip_odict(wrapped):

    @functools.wraps(wrapped)
    def strip(*args):
        return salt.utils.json.loads(salt.utils.json.dumps(wrapped(*args)))
    return strip