def opls_notation(atom_key):
    conflicts = ['ne', 'he', 'na']
    if atom_key in conflicts:
        raise _AtomKeyConflict(
            "One of the OPLS conflicting atom_keys has occured '{0}'. For how to solve this issue see the manual or MolecularSystem._atom_key_swap() doc string."
            .format(atom_key))
    for element in opls_atom_keys:
        if atom_key in opls_atom_keys[element]:
            return element
    raise _AtomKeyError(
        'OPLS atom key {0} was not found in OPLS keys dictionary.'.format(
        atom_key))