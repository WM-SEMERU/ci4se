def srp(x, promisc=None, iface=None, iface_hint=None, filter=None, nofilter
    =0, type=ETH_P_ALL, *args, **kargs):
    if iface is None and iface_hint is not None:
        iface = conf.route.route(iface_hint)[0]
    s = conf.L2socket(promisc=promisc, iface=iface, filter=filter, nofilter
        =nofilter, type=type)
    result = sndrcv(s, x, *args, **kargs)
    s.close()
    return result