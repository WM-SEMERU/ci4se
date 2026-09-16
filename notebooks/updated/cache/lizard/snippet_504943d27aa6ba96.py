def nla_ok(nla, remaining):
    return (remaining.value >= nla.SIZEOF and nla.SIZEOF <= nla.nla_len <=
        remaining.value)