def get_atom_mapping(self):
    smiles_to_pdb_mapping = self.bindingsite.xpath(
        'mappings/smiles_to_pdb/text()')
    if smiles_to_pdb_mapping == []:
        self.mappings = {'smiles_to_pdb': None, 'pdb_to_smiles': None}
    else:
        smiles_to_pdb_mapping = {int(y[0]): int(y[1]) for y in [x.split(':'
            ) for x in smiles_to_pdb_mapping[0].split(',')]}
        self.mappings = {'smiles_to_pdb': smiles_to_pdb_mapping}
        self.mappings['pdb_to_smiles'] = {v: k for k, v in self.mappings[
            'smiles_to_pdb'].items()}