def variantcall_sample(data, region=None, align_bams=None, out_file=None):
    if out_file is None or not os.path.exists(out_file) or not os.path.lexists(
        out_file):
        utils.safe_makedir(os.path.dirname(out_file))
        ref_file = dd.get_ref_file(data)
        config = data['config']
        caller_fns = get_variantcallers()
        caller_fn = caller_fns[config['algorithm'].get('variantcaller')]
        if len(align_bams) == 1:
            items = [data]
        else:
            items = multi.get_orig_items(data)
            assert len(items) == len(align_bams)
        assoc_files = tz.get_in(('genome_resources', 'variation'), data, {})
        if not assoc_files:
            assoc_files = {}
        for bam_file in align_bams:
            bam.index(bam_file, data['config'], check_timestamp=False)
        out_file = caller_fn(align_bams, items, ref_file, assoc_files,
            region, out_file)
    if region:
        data['region'] = region
    data['vrn_file'] = out_file
    return [data]