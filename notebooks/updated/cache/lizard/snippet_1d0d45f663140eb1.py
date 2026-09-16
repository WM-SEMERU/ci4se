def _prep_inputs(vrn_info, cnv_info, somatic_info, work_dir, config):
    exe = os.path.join(os.path.dirname(sys.executable),
        'create_phylowgs_inputs.py')
    assert os.path.exists(exe
        ), 'Could not find input prep script for PhyloWGS runs.'
    ssm_file = os.path.join(work_dir, 'ssm_data.txt')
    cnv_file = os.path.join(work_dir, 'cnv_data.txt')
    if not utils.file_exists(ssm_file) or not utils.file_exists(cnv_file):
        with file_transaction(somatic_info.tumor_data, ssm_file, cnv_file) as (
            tx_ssm_file, tx_cnv_file):
            variant_type, input_vcf_file = _prep_vrn_file(vrn_info[
                'vrn_file'], vrn_info['variantcaller'], work_dir,
                somatic_info, cnv_info['ignore'], config)
            input_cnv_file = _prep_cnv_file(cnv_info['subclones'], work_dir,
                somatic_info)
            cmd = [sys.executable, exe, '--sample-size', str(config[
                'sample_size']), '--tumor-sample', somatic_info.tumor_name,
                '--battenberg', input_cnv_file, '--cellularity',
                _read_contam(cnv_info['contamination']), '--output-cnvs',
                tx_cnv_file, '--output-variants', tx_ssm_file,
                '--variant-type', variant_type, input_vcf_file]
            do.run(cmd, 'Prepare PhyloWGS inputs.')
    return ssm_file, cnv_file