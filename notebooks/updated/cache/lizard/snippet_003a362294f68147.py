def xrb_address_to_public_key(address):
    address = bytearray(address, 'ascii')
    if not address.startswith(b'xrb_'):
        raise ValueError('address does not start with xrb_: %s' % address)
    if len(address) != 64:
        raise ValueError('address must be 64 chars long: %s' % address)
    address = bytes(address)
    key_b32xrb = b'1111' + address[4:56]
    key_bytes = b32xrb_decode(key_b32xrb)[3:]
    checksum = address[56:]
    if b32xrb_encode(address_checksum(key_bytes)) != checksum:
        raise ValueError('invalid address, invalid checksum: %s' % address)
    return key_bytes