def fetch_mga_scores(mga_vec, codon_pos, default_mga=None):
    len_mga = len(mga_vec)
    good_codon_pos = [p for p in codon_pos if p < len_mga]
    if good_codon_pos:
        mga_ent_scores = mga_vec[good_codon_pos]
    else:
        mga_ent_scores = None
    return mga_ent_scores