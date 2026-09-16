def parallel_prep_region(samples, run_parallel):
    file_key = 'work_bam'
    split_fn = _split_by_regions('bamprep', '-prep.bam', file_key)
    extras = []
    torun = []
    for data in [x[0] for x in samples]:
        if data.get('work_bam'):
            data['align_bam'] = data['work_bam']
        if not dd.get_realign(data) and not dd.get_variantcaller(data):
            extras.append([data])
        elif not data.get(file_key):
            extras.append([data])
        else:
            data['config']['algorithm']['orig_markduplicates'
                ] = dd.get_mark_duplicates(data)
            data = dd.set_mark_duplicates(data, False)
            torun.append([data])
    return extras + parallel_split_combine(torun, split_fn, run_parallel,
        'piped_bamprep', _add_combine_info, file_key, ['config'])