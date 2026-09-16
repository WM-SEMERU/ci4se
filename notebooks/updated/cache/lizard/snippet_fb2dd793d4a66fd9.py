def filter_on_wire_representation(ava, acs, required=None, optional=None):
    acsdic = dict([(ac.name_format, ac) for ac in acs])
    if required is None:
        required = []
    if optional is None:
        optional = []
    res = {}
    for attr, val in ava.items():
        done = False
        for req in required:
            try:
                _name = acsdic[req.name_format]._to[attr]
                if _name == req.name:
                    res[attr] = val
                    done = True
            except KeyError:
                pass
        if done:
            continue
        for opt in optional:
            try:
                _name = acsdic[opt.name_format]._to[attr]
                if _name == opt.name:
                    res[attr] = val
                    break
            except KeyError:
                pass
    return res