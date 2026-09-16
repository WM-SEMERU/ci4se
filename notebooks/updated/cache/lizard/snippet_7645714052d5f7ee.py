def _apply_local_transforms(p, ts):
    p_corrected = _bitstring_probs_by_qubit(p)
    nq = p_corrected.ndim
    for idx, trafo_idx in enumerate(ts):
        einsum_pat = 'ij,' + _CHARS[:idx] + 'j' + _CHARS[idx:nq - 1
            ] + '->' + _CHARS[:idx] + 'i' + _CHARS[idx:nq - 1]
        p_corrected = np.einsum(einsum_pat, trafo_idx, p_corrected)
    return p_corrected