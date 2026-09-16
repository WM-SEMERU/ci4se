def get_rdns_name(rdns):
    name = ''
    for rdn in rdns:
        for attr in rdn._attributes:
            if len(name) > 0:
                name = name + ','
            if attr.oid in OID_NAMES:
                name = name + OID_NAMES[attr.oid]
            else:
                name = name + attr.oid._name
            name = name + '=' + attr.value
    return name