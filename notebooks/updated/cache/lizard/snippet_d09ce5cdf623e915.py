def set_packet_headers(self, headers):
    bin_headers = '0x' + binascii.hexlify(headers.bin()).decode('utf-8')
    self.set_attributes(ps_packetheader=bin_headers)
    body_handler = headers
    ps_headerprotocol = []
    while body_handler:
        segment = pypacker_2_xena.get(str(body_handler).split('(')[0].lower
            (), None)
        if not segment:
            self.logger.warning('pypacker header {} not in conversion list'
                .format(segment))
            return
        ps_headerprotocol.append(segment)
        if type(body_handler) is Ethernet and body_handler.vlan:
            ps_headerprotocol.append('vlan')
        body_handler = body_handler.body_handler
    self.set_attributes(ps_headerprotocol=' '.join(ps_headerprotocol))