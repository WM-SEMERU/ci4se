async def start_pairing(self):
    self.srp.initialize()
    msg = messages.crypto_pairing({tlv8.TLV_METHOD: b'\x00', tlv8.
        TLV_SEQ_NO: b'\x01'})
    resp = await self.protocol.send_and_receive(msg, generate_identifier=False)
    pairing_data = _get_pairing_data(resp)
    if tlv8.TLV_BACK_OFF in pairing_data:
        time = int.from_bytes(pairing_data[tlv8.TLV_BACK_OFF], byteorder='big')
        raise Exception('back off {0}s'.format(time))
    self._atv_salt = pairing_data[tlv8.TLV_SALT]
    self._atv_pub_key = pairing_data[tlv8.TLV_PUBLIC_KEY]