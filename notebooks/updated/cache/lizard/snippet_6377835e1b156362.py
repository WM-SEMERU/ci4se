def blockstack_tx_filter(tx):
    if not 'nulldata' in tx:
        return False
    if tx['nulldata'] is None:
        return False
    payload = binascii.unhexlify(tx['nulldata'])
    if payload.startswith(blockstack_magic_bytes()):
        return True
    else:
        return False