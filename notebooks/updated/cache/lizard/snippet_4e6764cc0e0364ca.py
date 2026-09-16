def from_bytes(rawbytes):
    icmpv6popts = ICMPv6OptionList()
    i = 0
    while i < len(rawbytes):
        opttype = rawbytes[i]
        optnum = ICMPv6OptionNumber(opttype)
        obj = ICMPv6OptionClasses[optnum]()
        eaten = obj.from_bytes(rawbytes[i:])
        i += eaten
        icmpv6popts.append(obj)
    return icmpv6popts