def to_bam(in_file, out_file, data):
    if not utils.file_uptodate(out_file, in_file):
        with file_transaction(data, out_file) as tx_out_file:
            cmd = ['samtools', 'view', '-O', 'BAM', '-o', tx_out_file, in_file]
            do.run(cmd, 'Convert CRAM to BAM')
    bam.index(out_file, data['config'])
    return out_file