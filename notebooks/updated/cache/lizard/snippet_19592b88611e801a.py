def from_jsondict(cls, dict_):
    fields = [ofproto.oxs_from_jsondict(f) for f in dict_['oxs_fields']]
    return OFPStats(_ordered_fields=fields)