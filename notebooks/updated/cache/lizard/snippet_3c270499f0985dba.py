def get_lldp_tlv(self, port_name, is_ncb=True, is_nb=False):
    reply = None
    if is_ncb:
        reply = self.run_lldptool(['get-tlv', '-n', '-i', port_name, '-g',
            'ncb'])
    elif is_nb:
        reply = self.run_lldptool(['get-tlv', '-n', '-i', port_name, '-g',
            'nb'])
    else:
        LOG.error('Both NCB and NB are not selected to query LLDP')
    return reply