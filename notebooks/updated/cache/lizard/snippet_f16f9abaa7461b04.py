def peptide_mutation_interval(peptide_start_in_protein, peptide_length,
    mutation_start_in_protein, mutation_end_in_protein):
    if peptide_start_in_protein > mutation_end_in_protein:
        raise ValueError('Peptide starts after mutation')
    elif peptide_start_in_protein + peptide_length < mutation_start_in_protein:
        raise ValueError('Peptide ends before mutation')
    peptide_mutation_start_offset = min(peptide_length, max(0, 
        mutation_start_in_protein - peptide_start_in_protein))
    peptide_mutation_end_offset = min(peptide_length, max(0, 
        mutation_end_in_protein - peptide_start_in_protein))
    return peptide_mutation_start_offset, peptide_mutation_end_offset