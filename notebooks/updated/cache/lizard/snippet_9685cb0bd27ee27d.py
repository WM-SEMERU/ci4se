def ec_construct_public(num):
    ecpn = ec.EllipticCurvePublicNumbers(num['x'], num['y'], NIST2SEC[
        as_unicode(num['crv'])]())
    return ecpn.public_key(default_backend())