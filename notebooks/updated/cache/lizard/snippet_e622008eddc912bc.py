def run(bam_file, data, out_dir):
    m = {'base': None, 'secondary': []}
    m.update(_mirbase_stats(data, out_dir))
    m['secondary'].append(_seqcluster_stats(data, out_dir))