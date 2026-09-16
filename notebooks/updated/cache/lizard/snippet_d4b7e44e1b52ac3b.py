def apply_substitutions(monomial, monomial_substitutions, pure=False):
    if is_number_type(monomial):
        return monomial
    original_monomial = monomial
    changed = True
    if not pure:
        substitutions = monomial_substitutions
    else:
        substitutions = {}
        for lhs, rhs in monomial_substitutions.items():
            irrelevant = False
            for atom in lhs.atoms():
                if atom.is_Number:
                    continue
                if not monomial.has(atom):
                    irrelevant = True
                    break
            if not irrelevant:
                substitutions[lhs] = rhs
    while changed:
        for lhs, rhs in substitutions.items():
            monomial = fast_substitute(monomial, lhs, rhs)
        if original_monomial == monomial:
            changed = False
        original_monomial = monomial
    return monomial