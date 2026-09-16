async def get_payment_info(self):
    if not hasattr(Credential.get_payment_info, 'cb'):
        self.logger.debug('vcx_credential_get_payment_info: Creating callback')
        Credential.get_payment_info.cb = create_cb(CFUNCTYPE(None, c_uint32,
            c_uint32, c_char_p))
    c_credential_handle = c_uint32(self.handle)
    data = await do_call('vcx_credential_get_payment_info',
        c_credential_handle, Credential.get_payment_info.cb)
    return json.loads(data.decode())