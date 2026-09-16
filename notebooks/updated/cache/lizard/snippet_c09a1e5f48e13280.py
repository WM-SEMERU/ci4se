def _to_ctfile_atom_block(self, key):
    counter = OrderedCounter(Atom.atom_block_format)
    ctab_atom_block = '\n'.join([''.join([str(value).rjust(spacing) for 
        value, spacing in zip(atom._ctab_data.values(), counter.values())]) for
        atom in self[key]])
    return '{}\n'.format(ctab_atom_block)