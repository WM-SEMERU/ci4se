def verify_signature(key, qs):
    unsigned_qs = re.sub('&?sig=[^&]*', '', qs)
    sig = derive_signature(key, unsigned_qs)
    return urlparse.parse_qs(qs).get('sig', [None])[0] == sig