def SetProtocol(self, protocol):
    protocol = protocol.lower().strip()
    if protocol not in ['http', 'https']:
        raise ValueError('Invalid protocol specified for Viper lookup')
    self._analyzer.SetProtocol(protocol)