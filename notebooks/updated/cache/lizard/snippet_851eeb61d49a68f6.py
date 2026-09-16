def get_generic_subseq_2D(protein, cutoff, prop, condition):
    subseq, subseq_resnums = (protein.representative_sequence.
        get_subsequence_from_property(property_key=prop, property_value=
        cutoff, condition=condition, return_resnums=True) or (None, []))
    return {'subseq_len': len(subseq_resnums), 'subseq': subseq,
        'subseq_resnums': subseq_resnums}