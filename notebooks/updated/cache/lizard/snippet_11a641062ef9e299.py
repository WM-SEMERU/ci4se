def triads(reference_labels, estimated_labels):
    validate(reference_labels, estimated_labels)
    ref_roots, ref_semitones = encode_many(reference_labels, False)[:2]
    est_roots, est_semitones = encode_many(estimated_labels, False)[:2]
    eq_roots = ref_roots == est_roots
    eq_semitones = np.all(np.equal(ref_semitones[:, :8], est_semitones[:, :
        8]), axis=1)
    comparison_scores = (eq_roots * eq_semitones).astype(np.float)
    comparison_scores[np.any(ref_semitones < 0, axis=1)] = -1.0
    return comparison_scores