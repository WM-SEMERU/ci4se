async def send_request(self, connection: Connection, payment_handle: int):
    if not hasattr(Credential.send_request, 'cb'):
        self.logger.debug('vcx_credential_send_request: Creating callback')
        Credential.send_request.cb = create_cb(CFUNCTYPE(None, c_uint32,
            c_uint32))
    c_credential_handle = c_uint32(self.handle)
    c_connection_handle = c_uint32(connection.handle)
    c_payment = c_uint32(payment_handle)
    await do_call('vcx_credential_send_request', c_credential_handle,
        c_connection_handle, c_payment, Credential.send_request.cb)