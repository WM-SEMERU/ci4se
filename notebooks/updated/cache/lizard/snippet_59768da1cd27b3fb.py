def send(x, inter=0, loop=0, count=None, verbose=None, realtime=None, *args,
    **kargs):
    __gen_send(conf.L3socket(*args, **kargs), x, inter=inter, loop=loop,
        count=count, verbose=verbose, realtime=realtime)