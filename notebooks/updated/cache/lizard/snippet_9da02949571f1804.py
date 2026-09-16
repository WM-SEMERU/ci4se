def rotate(prefixes, hosts, **kwargs):
    rotator = Rotator(pyes.ES(hosts), **kwargs)
    for prefix in prefixes:
        rotator.rotate(prefix)