def _titan_cn_file(cnr_file, work_dir, data):
    out_file = os.path.join(work_dir, '%s.cn' % utils.splitext_plus(os.path
        .basename(cnr_file))[0])
    support_cols = {'cnvkit': ['chromosome', 'start', 'end', 'log2'],
        'gatk-cnv': ['CONTIG', 'START', 'END', 'LOG2_COPY_RATIO']}
    cols = support_cols[cnvkit.bin_approach(data)]
    if not utils.file_uptodate(out_file, cnr_file):
        with file_transaction(data, out_file) as tx_out_file:
            iterator = pd.read_table(cnr_file, sep='\t', iterator=True,
                header=0, comment='@')
            with open(tx_out_file, 'w') as handle:
                for chunk in iterator:
                    chunk = chunk[cols]
                    chunk.columns = ['chrom', 'start', 'end', 'logR']
                    if cnvkit.bin_approach(data) == 'cnvkit':
                        chunk['start'] += 1
                    chunk.to_csv(handle, mode='a', sep='\t', index=False)
    return out_file