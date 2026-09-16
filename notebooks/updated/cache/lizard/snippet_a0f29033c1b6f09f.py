def _check_umi_type(bam_file):
    with pysam.Samfile(bam_file, 'rb') as in_bam:
        for read in in_bam:
            cur_umi = None
            for tag in ['RX', 'XC']:
                try:
                    cur_umi = read.get_tag(tag)
                    break
                except KeyError:
                    pass
            if cur_umi:
                if '-' in cur_umi and len(cur_umi.split('-')) == 2:
                    return 'paired', tag
                else:
                    return 'adjacency', tag