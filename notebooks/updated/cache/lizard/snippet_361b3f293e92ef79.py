def keys_by_alg_and_usage(self, issuer, alg, usage):
    if usage in ['sig', 'ver']:
        ktype = jws_alg2keytype(alg)
    else:
        ktype = jwe_alg2keytype(alg)
    return self.get(usage, ktype, issuer)