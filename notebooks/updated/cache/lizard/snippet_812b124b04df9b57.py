def genlmsg_put(msg, port, seq, family, hdrlen, flags, cmd, version):
    hdr = genlmsghdr(cmd=cmd, version=version)
    nlh = nlmsg_put(msg, port, seq, family, GENL_HDRLEN + hdrlen, flags)
    if nlh is None:
        return None
    nlmsg_data(nlh)[:hdr.SIZEOF] = hdr.bytearray[:hdr.SIZEOF]
    _LOGGER.debug('msg 0x%x: Added generic netlink header cmd=%d version=%d',
        id(msg), cmd, version)
    return bytearray_ptr(nlmsg_data(nlh), GENL_HDRLEN)