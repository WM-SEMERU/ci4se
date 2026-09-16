def reverse_translate(protein_seq, template_dna=None, leading_seq=None,
    trailing_seq=None, forbidden_seqs=(), include_stop=True, manufacturer=None
    ):
    if manufacturer == 'gen9':
        forbidden_seqs += gen9.reserved_restriction_sites
    leading_seq = restriction_sites.get(leading_seq, leading_seq or '')
    trailing_seq = restriction_sites.get(trailing_seq, trailing_seq or '')
    codon_list = make_codon_list(protein_seq, template_dna, include_stop)
    sanitize_codon_list(codon_list, forbidden_seqs)
    dna_seq = leading_seq + ''.join(codon_list) + trailing_seq
    if manufacturer == 'gen9':
        gen9.apply_quality_control_checks(dna_seq)
    return dna_seq