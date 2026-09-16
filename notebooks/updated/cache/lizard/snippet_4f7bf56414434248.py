def _topology_from_parmed(structure, non_element_types):
    topology = app.Topology()
    residues = dict()
    for pmd_residue in structure.residues:
        chain = topology.addChain()
        omm_residue = topology.addResidue(pmd_residue.name, chain)
        residues[pmd_residue] = omm_residue
    atoms = dict()
    for pmd_atom in structure.atoms:
        name = pmd_atom.name
        if pmd_atom.name in non_element_types:
            element = non_element_types[pmd_atom.name]
        elif isinstance(pmd_atom.atomic_number, int
            ) and pmd_atom.atomic_number != 0:
            element = elem.Element.getByAtomicNumber(pmd_atom.atomic_number)
        else:
            element = elem.Element.getBySymbol(pmd_atom.name)
        omm_atom = topology.addAtom(name, element, residues[pmd_atom.residue])
        atoms[pmd_atom] = omm_atom
        omm_atom.bond_partners = []
    for bond in structure.bonds:
        atom1 = atoms[bond.atom1]
        atom2 = atoms[bond.atom2]
        topology.addBond(atom1, atom2)
        atom1.bond_partners.append(atom2)
        atom2.bond_partners.append(atom1)
    if structure.box_vectors and np.any([x._value for x in structure.
        box_vectors]):
        topology.setPeriodicBoxVectors(structure.box_vectors)
    positions = structure.positions
    return topology, positions