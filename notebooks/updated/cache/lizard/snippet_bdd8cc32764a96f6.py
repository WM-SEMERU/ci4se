def mw_wo_sw(mol, ndigits=2):
    cp = clone(mol)
    remover.remove_water(cp)
    remover.remove_salt(cp)
    return round(sum(a.mw() for _, a in cp.atoms_iter()), ndigits)