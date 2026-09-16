def matches_ip(cls, ip_str, read_preference=None):
    qs = cls.qs_for_ip(ip_str).only('whitelist')
    if read_preference:
        qs = qs.read_preference(read_preference)
    return bool(qs) and not any(obj.whitelist for obj in qs)