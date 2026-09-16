def _prep_callable_bed(in_file, work_dir, stats, data):
    out_file = os.path.join(work_dir, '%s-merge.bed.gz' % utils.
        splitext_plus(os.path.basename(in_file))[0])
    gsort = config_utils.get_program('gsort', data)
    if not utils.file_uptodate(out_file, in_file):
        with file_transaction(data, out_file) as tx_out_file:
            fai_file = ref.fasta_idx(dd.get_ref_file(data))
            cmd = (
                '{gsort} {in_file} {fai_file} | bedtools merge -i - -d {stats[merge_size]} | bgzip -c > {tx_out_file}'
                )
            do.run(cmd.format(**locals()), 'Prepare SV callable BED regions')
    return vcfutils.bgzip_and_index(out_file, data['config'])