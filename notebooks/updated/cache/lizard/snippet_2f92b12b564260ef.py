def dispatch_hook(cls, _pkt=b'', *args, **kargs):
    if _pkt and len(_pkt) >= 1:
        if orb(_pkt[0]) == 65:
            return LoWPANUncompressedIPv6
        if orb(_pkt[0]) == 66:
            return LoWPAN_HC1
        if orb(_pkt[0]) >> 3 == 24:
            return LoWPANFragmentationFirst
        elif orb(_pkt[0]) >> 3 == 28:
            return LoWPANFragmentationSubsequent
        elif orb(_pkt[0]) >> 6 == 2:
            return LoWPANMesh
        elif orb(_pkt[0]) >> 6 == 1:
            return LoWPAN_IPHC
    return cls