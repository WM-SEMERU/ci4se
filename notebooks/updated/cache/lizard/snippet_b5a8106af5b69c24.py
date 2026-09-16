def ensure_ec_params(jwk_dict, private):
    provided = frozenset(jwk_dict.keys())
    if private is not None and private:
        required = EC_PUBLIC_REQUIRED | EC_PRIVATE_REQUIRED
    else:
        required = EC_PUBLIC_REQUIRED
    return ensure_params('EC', provided, required)