def set_trace(*args, **kwargs):
    out = sys.stdout.stream if hasattr(sys.stdout, 'stream') else None
    kwargs['stdout'] = out
    debugger = pdb.Pdb(*args, **kwargs)
    debugger.use_rawinput = True
    debugger.set_trace(sys._getframe().f_back)