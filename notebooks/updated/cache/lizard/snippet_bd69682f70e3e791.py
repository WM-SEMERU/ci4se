def _cluster(bam_file, ma_file, out_dir, reference, annotation_file=None):
    seqcluster = op.join(get_bcbio_bin(), 'seqcluster')
    if annotation_file:
        annotation_file = '-g ' + annotation_file
    else:
        annotation_file = ''
    if not file_exists(op.join(out_dir, 'counts.tsv')):
        cmd = (
            '{seqcluster} cluster -o {out_dir} -m {ma_file} -a {bam_file} -r {reference} {annotation_file}'
            )
        do.run(cmd.format(**locals()), 'Running seqcluster.')
    counts = op.join(out_dir, 'counts.tsv')
    stats = op.join(out_dir, 'read_stats.tsv')
    json = op.join(out_dir, 'seqcluster.json')
    return {'out_dir': out_dir, 'count_file': counts, 'stat_file': stats,
        'json': json}