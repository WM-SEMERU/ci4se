def molecule(lines):
    count_line = lines[3]
    num_atoms = int(count_line[0:3])
    num_bonds = int(count_line[3:6])
    compound = Compound()
    compound.graph._node = atoms(lines[4:num_atoms + 4])
    compound.graph._adj = bonds(lines[num_atoms + 4:num_atoms + num_bonds +
        4], compound.graph._node.keys())
    props = properties(lines[num_atoms + num_bonds + 4:])
    add_properties(props, compound)
    return compound