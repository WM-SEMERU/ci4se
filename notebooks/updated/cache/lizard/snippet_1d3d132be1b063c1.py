def lookup_ip(self, mac):
    res = self.lookup_by_lease(mac=mac)
    try:
        return res['ip-address']
    except KeyError:
        raise OmapiErrorAttributeNotFound()