def umi_transform(data):
    fq1 = data['files'][0]
    umi_dir = os.path.join(dd.get_work_dir(data), 'umis')
    safe_makedir(umi_dir)
    transform = dd.get_umi_type(data)
    if not transform:
        logger.info(
            'No UMI transform specified, assuming pre-transformed data.')
        if is_transformed(fq1):
            logger.info(
                '%s detected as pre-transformed, passing it on unchanged.' %
                fq1)
            data['files'] = [fq1]
            return data
        else:
            logger.error(
                'No UMI transform was specified, but %s does not look pre-transformed. Assuming non-umi data.'
                 % fq1)
            return data
    if file_exists(transform):
        transform_file = transform
    else:
        transform_file = get_transform_file(transform)
        if not file_exists(transform_file):
            logger.error(
                'The UMI transform can be specified as either a file or a bcbio-supported transform. Either the file %s does not exist or the transform is not supported by bcbio. Supported transforms are %s.'
                 % (dd.get_umi_type(data), ', '.join(SUPPORTED_TRANSFORMS)))
            sys.exit(1)
    out_base = dd.get_sample_name(data) + '.umitransformed.fq.gz'
    out_file = os.path.join(umi_dir, out_base)
    if file_exists(out_file):
        data['files'] = [out_file]
        return data
    umis = config_utils.get_program('umis', data, default='umis')
    cores = dd.get_num_cores(data)
    with open_fastq(fq1) as in_handle:
        read = next(in_handle)
        if 'UMI_' in read:
            data['files'] = [out_file]
            return data
    cmd = (
        '{umis} fastqtransform {transform_file} --cores {cores} {fq1}| seqtk seq -L 20 - | gzip > {tx_out_file}'
        )
    message = (
        'Inserting UMI and barcode information into the read name of %s' % fq1)
    with file_transaction(out_file) as tx_out_file:
        do.run(cmd.format(**locals()), message)
    data['files'] = [out_file]
    return data