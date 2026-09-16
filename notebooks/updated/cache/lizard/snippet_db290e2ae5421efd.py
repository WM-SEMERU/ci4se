def tdecode(pktlist, args=None, **kwargs):
    if args is None:
        args = ['-V']
    return tcpdump(pktlist, prog=conf.prog.tshark, args=args, **kwargs)