def create(gandi, resource, flags, algorithm, public_key):
    result = gandi.dnssec.create(resource, flags, algorithm, public_key)
    return result