def _cutadapt_trim(fastq_files, quality_format, adapters, out_files,
    log_file, data):
    if all([utils.file_exists(x) for x in out_files]):
        return out_files
    cmd = _cutadapt_trim_cmd(fastq_files, quality_format, adapters,
        out_files, data)
    if len(fastq_files) == 1:
        of = [out_files[0], log_file]
        message = ('Trimming %s in single end mode with cutadapt.' %
            fastq_files[0])
        with file_transaction(data, of) as of_tx:
            of1_tx, log_tx = of_tx
            do.run(cmd.format(**locals()), message)
    else:
        of = out_files + [log_file]
        with file_transaction(data, of) as tx_out_files:
            of1_tx, of2_tx, log_tx = tx_out_files
            tmp_fq1 = utils.append_stem(of1_tx, '.tmp')
            tmp_fq2 = utils.append_stem(of2_tx, '.tmp')
            singles_file = of1_tx + '.single'
            message = (
                'Trimming %s and %s in paired end mode with cutadapt.' % (
                fastq_files[0], fastq_files[1]))
            do.run(cmd.format(**locals()), message)
    return out_files