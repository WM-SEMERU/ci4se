def majmin_inv(reference_labels, estimated_labels):
    validate(reference_labels, estimated_labels)
    maj_semitones = np.array(QUALITIES['maj'][:8])
    min_semitones = np.array(QUALITIES['min'][:8])
    ref_roots, ref_semitones, ref_bass = encode_many(reference_labels, False)
    est_roots, est_semitones, est_bass = encode_many(estimated_labels, False)
    eq_root_bass = (ref_roots == est_roots) * (ref_bass == est_bass)
    eq_semitones = np.all(np.equal(ref_semitones[:, :8], est_semitones[:, :
        8]), axis=1)
    comparison_scores = (eq_root_bass * eq_semitones).astype(np.float)
    is_maj = np.all(np.equal(ref_semitones[:, :8], maj_semitones), axis=1)
    is_min = np.all(np.equal(ref_semitones[:, :8], min_semitones), axis=1)
    is_none = np.logical_and(ref_roots < 0, np.all(ref_semitones == 0, axis=1))
    comparison_scores[is_maj + is_min + is_none == 0] = -1
    valid_inversion = np.ones(ref_bass.shape, dtype=bool)
    bass_idx = ref_bass >= 0
    valid_inversion[bass_idx] = ref_semitones[bass_idx, ref_bass[bass_idx]]
    comparison_scores[valid_inversion == 0] = -1
    return comparison_scores