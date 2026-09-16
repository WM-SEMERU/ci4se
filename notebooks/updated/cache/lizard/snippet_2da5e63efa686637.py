def create(cls, fqdn, flags, algorithm, public_key):
    fqdn = fqdn.lower()
    params = {'flags': flags, 'algorithm': algorithm, 'public_key': public_key}
    result = cls.call('domain.dnssec.create', fqdn, params)
    return result