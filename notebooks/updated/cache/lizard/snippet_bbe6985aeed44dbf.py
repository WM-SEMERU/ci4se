def make_pkh_address(pubkey, witness=False, cashaddr=True):
    pubkey_hash = utils.hash160(pubkey)
    return _make_pkh_address(pubkey_hash=pubkey_hash, witness=witness,
        cashaddr=cashaddr)