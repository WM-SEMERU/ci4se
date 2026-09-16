def run(name, chip_bam, input_bam, genome_build, out_dir, method, resources,
    data):
    config = dd.get_config(data)
    out_file = os.path.join(out_dir, name + '_peaks_macs2.xls')
    macs2_file = os.path.join(out_dir, name + '_peaks.xls')
    if utils.file_exists(out_file):
        _compres_bdg_files(out_dir)
        return _get_output_files(out_dir)
    macs2 = config_utils.get_program('macs2', config)
    options = ' '.join(resources.get('macs2', {}).get('options', ''))
    genome_size = bam.fasta.total_sequence_length(dd.get_ref_file(data))
    genome_size = '' if options.find('-g') > -1 else '-g %s' % genome_size
    paired = '-f BAMPE' if bam.is_paired(chip_bam) else ''
    with utils.chdir(out_dir):
        cmd = _macs2_cmd(method)
        try:
            do.run(cmd.format(**locals()), 'macs2 for %s' % name)
            utils.move_safe(macs2_file, out_file)
        except subprocess.CalledProcessError:
            raise RuntimeWarning(
                """macs2 terminated with an error.
Please, check the message and report error if it is related to bcbio.
You can add specific options for the sample setting resources as explained in docs: https://bcbio-nextgen.readthedocs.org/en/latest/contents/configuration.html#sample-specific-resources"""
                )
    _compres_bdg_files(out_dir)
    return _get_output_files(out_dir)