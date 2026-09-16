def verify(address, plaintext, scriptSigb64):
    assert isinstance(address, str)
    assert isinstance(scriptSigb64, str)
    scriptSig = base64.b64decode(scriptSigb64)
    hash_hex = hashlib.sha256(plaintext).hexdigest()
    vb = keylib.b58check.b58check_version_byte(address)
    if vb == bitcoin_blockchain.version_byte:
        return verify_singlesig(address, hash_hex, scriptSig)
    elif vb == bitcoin_blockchain.multisig_version_byte:
        return verify_multisig(address, hash_hex, scriptSig)
    else:
        log.warning('Unrecognized address version byte {}'.format(vb))
        raise NotImplementedError(
            'Addresses must be single-sig (version-byte = 0) or multi-sig (version-byte = 5)'
            )