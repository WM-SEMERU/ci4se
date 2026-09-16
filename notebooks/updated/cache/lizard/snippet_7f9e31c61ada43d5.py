def get_sequence_tooltips(self, pdb_object, pdb_sequence, pdb_sequence_type,
    pdb_name, pdb_chain, pdb_alignment_lines):
    raise Exception('Re-implement using the equivalence classes.')
    tooltips = None
    atom_sequence = pdb_object.atom_sequences.get(pdb_chain)
    try:
        if pdb_sequence_type == 'SEQRES':
            seqres_to_atom_map = self.seqres_to_atom_maps.get(pdb_name, {}
                ).get(pdb_chain, {})
            tooltips = []
            if seqres_to_atom_map:
                idx = 1
                for aligned_residue in pdb_alignment_lines.strip():
                    if aligned_residue != '-':
                        atom_residue = seqres_to_atom_map.get(idx)
                        if atom_residue:
                            assert aligned_residue == atom_sequence.sequence[
                                atom_residue].ResidueAA
                        tooltips.append(atom_residue)
                        idx += 1
                assert len(tooltips) == len(str(pdb_sequence))
        elif pdb_sequence_type == 'ATOM':
            tooltips = []
            idx = 0
            for aligned_residue in pdb_alignment_lines.strip():
                if aligned_residue != '-':
                    assert aligned_residue == pdb_sequence.sequence[
                        pdb_sequence.order[idx]].ResidueAA
                    tooltips.append(pdb_sequence.order[idx])
                    idx += 1
            assert len(tooltips) == len(str(pdb_sequence))
    except:
        raise Exception(
            'An error occurred during HTML tooltip creation for the multiple sequence alignment.'
            )
    return tooltips