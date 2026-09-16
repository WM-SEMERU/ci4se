def Asyncme(func, n=None, interval=0, default_callback=None, loop=None):
    return coros(n, interval, default_callback, loop)(func)