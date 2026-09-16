def mifare_classic_authenticate_block(self, uid, block_number, key_number, key
    ):
    uidlen = len(uid)
    keylen = len(key)
    params = bytearray(3 + uidlen + keylen)
    params[0] = 1
    params[1] = key_number & 255
    params[2] = block_number & 255
    params[3:3 + keylen] = key
    params[3 + keylen:] = uid
    response = self.call_function(PN532_COMMAND_INDATAEXCHANGE, params=
        params, response_length=1)
    return response[0] == 0