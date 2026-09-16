def _depr(fn, usage, stacklevel=3):
    warn('{0} is deprecated. Use {1} instead'.format(fn, usage), stacklevel
        =stacklevel, category=DeprecationWarning)