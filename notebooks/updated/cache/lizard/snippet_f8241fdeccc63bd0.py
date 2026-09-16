def build(self):
    ang_per_res = 2 * numpy.pi / self.residues_per_turn
    atom_offsets = _atom_offsets[self.helix_type]
    if self.handedness == 'l':
        handedness = -1
    else:
        handedness = 1
    atom_labels = ['N', 'CA', 'C', 'O']
    if all([(x in atom_offsets.keys()) for x in atom_labels]):
        res_label = 'GLY'
    else:
        res_label = 'UNK'
    monomers = []
    for i in range(self.num_monomers):
        residue = Residue(mol_code=res_label, ampal_parent=self)
        atoms_dict = OrderedDict()
        for atom_label in atom_labels:
            r, zeta, z_shift = atom_offsets[atom_label]
            rot_ang = (i * ang_per_res + zeta) * handedness
            z = self.rise_per_residue * i + z_shift
            coords = cylindrical_to_cartesian(radius=r, azimuth=rot_ang, z=
                z, radians=True)
            atom = Atom(coordinates=coords, element=atom_label[0],
                ampal_parent=residue, res_label=atom_label)
            atoms_dict[atom_label] = atom
        residue.atoms = atoms_dict
        monomers.append(residue)
    self._monomers = monomers
    self.relabel_monomers()
    self.relabel_atoms()
    return