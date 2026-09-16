def usable_id(cls, id):
    hcs = cls.from_fqdn(id)
    if hcs:
        return [hc_['id'] for hc_ in hcs]
    try:
        return int(id)
    except (TypeError, ValueError):
        pass