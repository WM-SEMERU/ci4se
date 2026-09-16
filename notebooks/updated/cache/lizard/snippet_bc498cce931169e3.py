def _prep_subsampled_bams(data, work_dir):
    sr_bam, disc_bam = sshared.get_split_discordants(data, work_dir)
    ds_bam = bam.downsample(dd.get_align_bam(data), data, 100000000.0,
        read_filter="-F 'not secondary_alignment and proper_pair'",
        always_run=True, work_dir=work_dir)
    out_bam = '%s-final%s' % utils.splitext_plus(ds_bam)
    if not utils.file_exists(out_bam):
        bam.merge([ds_bam, sr_bam, disc_bam], out_bam, data['config'])
    bam.index(out_bam, data['config'])
    return [out_bam]