def chose_blacklist(self, ip):
    blacklist = 'ellis_blacklist{0}'
    try:
        address = ipaddress.ip_address(ip)
    except ipaddress.AddressValueError:
        raise
    else:
        if address.version is 6:
            if address.is_private:
                msg = "We don't ban private addresses ({0} given).".format(
                    address)
                raise ipaddress.AddressValueError(msg)
            elif address.ipv4_mapped is not None:
                address = address.ipv4_mapped
            elif address.sixtofour is not None:
                address = address.sixtofour
    blacklist = blacklist.format(address.version)
    return address, blacklist