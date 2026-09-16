def get_blockcypher_walletname_from_mpub(mpub, subchain_indices=[]):
    mpub = mpub.encode('utf-8')
    if subchain_indices:
        mpub += ','.join([str(x) for x in subchain_indices]).encode('utf-8')
    return 'X%s' % sha256(mpub).hexdigest()[:24]