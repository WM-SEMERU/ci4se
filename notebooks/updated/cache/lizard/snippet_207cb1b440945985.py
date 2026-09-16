def _check_trim(data):
    trim = data['algorithm'].get('trim_reads')
    if trim:
        if trim == 'fastp' and data['algorithm'].get('align_split_size'
            ) is not False:
            raise ValueError(
                'In sample %s, `trim_reads: fastp` currently requires `align_split_size: false`'
                 % dd.get_sample_name(data))