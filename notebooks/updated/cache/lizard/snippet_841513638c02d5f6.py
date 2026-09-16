def _read_truth_freqs(in_file):
    out = {}
    with VariantFile(in_file) as bcf_in:
        for rec in bcf_in:
            freq = float(rec.info.get('VAF', 1.0))
            out[_get_key(rec)] = freq
    return out