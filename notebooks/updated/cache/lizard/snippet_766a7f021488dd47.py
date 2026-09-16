def varexp(line):
    ip = get_ipython()
    funcname, name = line.split()
    try:
        import guiqwt.pyplot as pyplot
    except:
        import matplotlib.pyplot as pyplot
    __fig__ = pyplot.figure()
    __items__ = getattr(pyplot, funcname[2:])(ip.user_ns[name])
    pyplot.show()
    del __fig__, __items__