def update_session(fname=None):
    if fname is None:
        fname = conf.session
    try:
        s = six.moves.cPickle.load(gzip.open(fname, 'rb'))
    except IOError:
        s = six.moves.cPickle.load(open(fname, 'rb'))
    scapy_session = six.moves.builtins.__dict__['scapy_session']
    scapy_session.update(s)
    update_ipython_session(scapy_session)