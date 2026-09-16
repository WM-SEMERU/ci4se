def configure_for_kerberos(self, datanode_transceiver_port=None,
    datanode_web_port=None):
    args = dict()
    if datanode_transceiver_port:
        args['datanodeTransceiverPort'] = datanode_transceiver_port
    if datanode_web_port:
        args['datanodeWebPort'] = datanode_web_port
    return self._cmd('configureForKerberos', data=args, api_version=11)