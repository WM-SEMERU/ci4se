def coros(n=None, interval=0, default_callback=None, loop=None):
    submitter = Loop(n=n, interval=interval, default_callback=
        default_callback, loop=loop).submitter
    return submitter