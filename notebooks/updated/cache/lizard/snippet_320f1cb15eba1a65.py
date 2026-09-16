def _get_input_args(bam_file, data, out_base, background):
    if dd.get_genome_build(data) in ['hg19']:
        return ['--PileupFile', _create_pileup(bam_file, data, out_base,
            background)]
    else:
        return ['--BamFile', bam_file]