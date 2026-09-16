def arping(net, timeout=2, cache=0, verbose=None, **kargs):
    if verbose is None:
        verbose = conf.verb
    ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=net),
        verbose=verbose, filter='arp and arp[7] = 2', timeout=timeout,
        iface_hint=net, **kargs)
    ans = ARPingResult(ans.res)
    if cache and ans is not None:
        for pair in ans:
            conf.netcache.arp_cache[pair[1].psrc] = pair[1].hwsrc, time.time()
    if verbose:
        ans.show()
    return ans, unans