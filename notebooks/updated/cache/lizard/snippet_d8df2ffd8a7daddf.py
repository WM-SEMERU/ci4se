def nla_for_each_nested(nla, rem):
    pos = nlattr(nla_data(nla))
    rem.value = nla_len(nla)
    while nla_ok(pos, rem):
        yield pos
        pos = nla_next(pos, rem)