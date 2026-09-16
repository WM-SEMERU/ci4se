def keys_delete(cls, fqdn, key):
    return cls.json_delete('%s/domains/%s/keys/%s' % (cls.api_url, fqdn, key))