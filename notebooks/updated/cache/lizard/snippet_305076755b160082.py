def inquire_by_mech(self, mech, name=True, init_lifetime=True,
    accept_lifetime=True, usage=True):
    res = rcreds.inquire_cred_by_mech(self, mech, name, init_lifetime,
        accept_lifetime, usage)
    if res.name is not None:
        res_name = names.Name(res.name)
    else:
        res_name = None
    return tuples.InquireCredByMechResult(res_name, res.init_lifetime, res.
        accept_lifetime, res.usage)