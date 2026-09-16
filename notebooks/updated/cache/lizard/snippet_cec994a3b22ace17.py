async def _connect(self, hostname, port, reconnect=False, password=None,
    encoding=pydle.protocol.DEFAULT_ENCODING, channels=[], tls=False,
    tls_verify=False, source_address=None):
    self.password = password
    if not reconnect:
        self._autojoin_channels = channels
        self.connection = connection.Connection(hostname, port,
            source_address=source_address, tls=tls, tls_verify=tls_verify,
            tls_certificate_file=self.tls_client_cert,
            tls_certificate_keyfile=self.tls_client_cert_key,
            tls_certificate_password=self.tls_client_cert_password,
            eventloop=self.eventloop)
        self.encoding = encoding
    await self.connection.connect()