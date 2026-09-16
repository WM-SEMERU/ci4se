def extract_xyz_matrix_from_pdb(pdb_lines, atoms_of_interest=backbone_atoms,
    expected_num_residues=None, expected_num_residue_atoms=None,
    fail_on_model_records=True, include_all_columns=False):
    if fail_on_model_records and [l for l in pdb_lines if l.startswith('MODEL')
        ]:
        raise Exception(
            'This function does not handle files with MODEL records. Please split those file by model first.'
            )
    chain_ids = set([l[21] for l in pdb_lines if l.startswith('ATOM  ')])
    dataframes = []
    for chain_id in chain_ids:
        dataframes.append(PDB.extract_xyz_matrix_from_pdb_chain(pdb_lines,
            chain_id, atoms_of_interest=atoms_of_interest,
            expected_num_residues=expected_num_residues,
            expected_num_residue_atoms=expected_num_residue_atoms,
            include_all_columns=include_all_columns))
    if dataframes:
        return pandas.concat(dataframes, verify_integrity=True)
    else:
        return None