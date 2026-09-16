def check_missing_atoms(self, template=None, ha_only=True):
    missing_atoms = {}
    if not template:
        import protein_residues
        template = protein_residues.normal
    for residue in self.get_residues():
        if not template.has_key(residue.resname):
            raise ValueError('Residue name (%s) not in the template' %
                residue.resname)
        if ha_only:
            heavy_atoms = [atom for atom in template[residue.resname][
                'atoms'].keys() if atom[0] != 'H' and not (atom[0].isdigit(
                ) and atom[1] == 'H')]
            reference_set = set(heavy_atoms)
        else:
            reference_set = set(template[residue.resname]['atoms'].keys())
        structure_set = set(residue.child_dict.keys())
        diff = reference_set.difference(structure_set)
        if diff:
            residue_uniq_id = (residue.parent.id, residue.resname, residue.
                get_id()[1])
            missing_atoms[residue_uniq_id] = list(diff)
    return missing_atoms