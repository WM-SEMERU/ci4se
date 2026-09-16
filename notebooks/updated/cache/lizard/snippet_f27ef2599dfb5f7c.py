def _is_small_vcf(vcf_file):
    count = 0
    small_thresh = 250
    with utils.open_gzipsafe(vcf_file) as in_handle:
        for line in in_handle:
            if not line.startswith('#'):
                count += 1
            if count > small_thresh:
                return False
    return True