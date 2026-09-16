def _concat_bgzip_fastq(finputs, out_dir, read, ldetail):
    out_file = os.path.join(out_dir, '%s_%s.fastq.gz' % (ldetail['name'], read)
        )
    if not utils.file_exists(out_file):
        with file_transaction(out_file) as tx_out_file:
            subprocess.check_call('zcat %s | bgzip -c > %s' % (' '.join(
                finputs), tx_out_file), shell=True)
    return out_file