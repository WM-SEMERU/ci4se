def _get_vqsr_training(filter_type, vrn_files, gatk_type):
    params = []
    for name, train_info, fname in _get_training_data(vrn_files)[filter_type]:
        if gatk_type == 'gatk4':
            params.extend(['--resource:%s,%s' % (name, train_info), fname])
            if filter_type == 'INDEL':
                params.extend(['--max-gaussians', '4'])
        else:
            params.extend(['-resource:%s,VCF,%s' % (name, train_info), fname])
            if filter_type == 'INDEL':
                params.extend(['--maxGaussians', '4'])
    return params