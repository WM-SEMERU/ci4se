def set_connection_params(self, ip_address, tsap_snap7, tsap_logo):
    assert re.match(ipv4, ip_address), '%s is invalid ipv4' % ip_address
    result = self.library.Cli_SetConnectionParams(self.pointer, ip_address.
        encode(), c_uint16(tsap_snap7), c_uint16(tsap_logo))
    if result != 0:
        raise Snap7Exception('The parameter was invalid')