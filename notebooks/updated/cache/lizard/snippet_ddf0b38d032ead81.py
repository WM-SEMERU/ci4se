def verify_bitcoin(message, signature, address):
    magic_sig = base64.b64decode(signature)
    magic = magic_sig[0]
    sig = Signature.from_bytes(magic_sig[1:])
    sig.recovery_id = magic - 27 & 3
    compressed = magic - 27 & 4 != 0
    msg = b'\x18Bitcoin Signed Message:\n' + bytes([len(message)]) + message
    msg_hash = hashlib.sha256(msg).digest()
    derived_public_key = PublicKey.from_signature(msg_hash, sig)
    if derived_public_key is None:
        raise ValueError(
            'Could not recover public key from the provided signature.')
    ver, h160 = address_to_key_hash(address)
    hash160 = derived_public_key.hash160(compressed)
    if hash160 != h160:
        return False
    return derived_public_key.verify(msg_hash, sig)