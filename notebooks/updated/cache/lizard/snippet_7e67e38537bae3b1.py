def from_dict(cls, parm, vrf=None):
    if vrf is None:
        vrf = VRF()
    vrf.id = parm['id']
    vrf.rt = parm['rt']
    vrf.name = parm['name']
    vrf.description = parm['description']
    vrf.tags = {}
    for tag_name in parm['tags']:
        tag = Tag.from_dict({'name': tag_name})
        vrf.tags[tag_name] = tag
    vrf.avps = parm['avps']
    vrf.num_prefixes_v4 = int(parm['num_prefixes_v4'])
    vrf.num_prefixes_v6 = int(parm['num_prefixes_v6'])
    vrf.total_addresses_v4 = int(parm['total_addresses_v4'])
    vrf.total_addresses_v6 = int(parm['total_addresses_v6'])
    vrf.used_addresses_v4 = int(parm['used_addresses_v4'])
    vrf.used_addresses_v6 = int(parm['used_addresses_v6'])
    vrf.free_addresses_v4 = int(parm['free_addresses_v4'])
    vrf.free_addresses_v6 = int(parm['free_addresses_v6'])
    return vrf