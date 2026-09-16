def _verify_support(identity, ecdh):
    protocol = identity.identity_dict['proto']
    if protocol not in {'ssh'}:
        raise NotImplementedError('Unsupported protocol: {}'.format(protocol))
    if ecdh:
        raise NotImplementedError('No support for ECDH')
    if identity.curve_name not in {formats.CURVE_NIST256}:
        raise NotImplementedError('Unsupported elliptic curve: {}'.format(
            identity.curve_name))