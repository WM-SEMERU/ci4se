def connectionMade(self):
    self.factory.request_xml = str(self.factory.payload)
    self.sendCommand('POST', '/cimom')
    self.sendHeader('Host', '%s:%d' % (self.transport.addr[0], self.
        transport.addr[1]))
    self.sendHeader('User-Agent', 'pywbem/twisted')
    self.sendHeader('Content-length', len(self.factory.payload))
    self.sendHeader('Content-type', 'application/xml')
    if self.factory.creds:
        auth = base64.b64encode('%s:%s' % (self.factory.creds[0], self.
            factory.creds[1]))
        self.sendHeader('Authorization', 'Basic %s' % auth)
    self.sendHeader('CIMOperation', str(self.factory.operation))
    self.sendHeader('CIMMethod', str(self.factory.method))
    self.sendHeader('CIMObject', str(self.factory.object))
    self.endHeaders()
    self.transport.write(str(self.factory.payload))