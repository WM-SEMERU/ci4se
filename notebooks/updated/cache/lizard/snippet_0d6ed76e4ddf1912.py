def nemo_accpars(Pot, vo, ro):
    Pot = flatten(Pot)
    if isinstance(Pot, list):
        out = ''
        for ii, pot in enumerate(Pot):
            if ii > 0:
                out += '#'
            out += pot.nemo_accpars(vo, ro)
        return out
    elif isinstance(Pot, Potential):
        return Pot.nemo_accpars(vo, ro)
    else:
        raise PotentialError(
            "Input to 'nemo_accpars' is neither a Potential-instance or a list of such instances"
            )