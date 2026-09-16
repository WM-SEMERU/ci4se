def signHash(self, message_hash, private_key):
    msg_hash_bytes = HexBytes(message_hash)
    if len(msg_hash_bytes) != 32:
        raise ValueError('The message hash must be exactly 32-bytes')
    key = self._parsePrivateKey(private_key)
    v, r, s, eth_signature_bytes = sign_message_hash(key, msg_hash_bytes)
    return AttributeDict({'messageHash': msg_hash_bytes, 'r': r, 's': s,
        'v': v, 'signature': HexBytes(eth_signature_bytes)})