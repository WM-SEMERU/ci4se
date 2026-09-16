def make_payment_script(address, blockchain='bitcoin', **blockchain_opts):
    if blockchain == 'bitcoin':
        return btc_make_payment_script(address, **blockchain_opts)
    else:
        raise ValueError("Unknown blockchain '{}'".format(blockchain))