def make_segwit_info(privkey=None):
    if privkey is None:
        privkey = BitcoinPrivateKey(compressed=True).to_wif()
    return make_multisig_segwit_info(1, [privkey])