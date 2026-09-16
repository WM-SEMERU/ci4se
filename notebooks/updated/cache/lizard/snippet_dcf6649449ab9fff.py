def _run_cnvkit_cancer(items, background):
    paired = vcfutils.get_paired_bams([x['align_bam'] for x in items], items)
    normal_data = [x for x in items if dd.get_sample_name(x) != paired.
        tumor_name]
    tumor_ready, normal_ready = _match_batches(paired.tumor_data, 
        normal_data[0] if normal_data else None)
    ckouts = _run_cnvkit_shared([tumor_ready], [normal_ready] if
        normal_ready else [])
    if not ckouts:
        return items
    assert len(ckouts) == 1
    tumor_data = _associate_cnvkit_out(ckouts, [paired.tumor_data],
        is_somatic=True)
    return tumor_data + normal_data