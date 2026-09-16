def process_wildcard(fractions):
    wildcard_zs = set()
    total_fraction = 0.0
    for z, fraction in fractions.items():
        if fraction == '?':
            wildcard_zs.add(z)
        else:
            total_fraction += fraction
    if not wildcard_zs:
        return fractions
    balance_fraction = (1.0 - total_fraction) / len(wildcard_zs)
    for z in wildcard_zs:
        fractions[z] = balance_fraction
    return fractions