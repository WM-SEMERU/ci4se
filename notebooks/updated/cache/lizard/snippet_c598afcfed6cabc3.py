def samblaster_dedup_sort(data, tx_out_file, tx_sr_file, tx_disc_file):
    samblaster = config_utils.get_program('samblaster', data['config'])
    samtools = config_utils.get_program('samtools', data['config'])
    tmp_prefix = '%s-sorttmp' % utils.splitext_plus(tx_out_file)[0]
    tobam_cmd = (
        '{samtools} sort {sort_opt} -@ {cores} -m {mem} -T {tmp_prefix}-{dext} {out_file} -'
        )
    cores, mem = _get_cores_memory(data, downscale=2)
    ds_cmd = None if data.get('align_split') else bam.get_maxcov_downsample_cl(
        data, 'samtools')
    sort_opt = '-n' if data.get('align_split') and dd.get_mark_duplicates(data
        ) else ''
    if ds_cmd:
        dedup_cmd = '%s %s > %s' % (tobam_cmd.format(out_file='', dext=
            'full', **locals()), ds_cmd, tx_out_file)
    else:
        dedup_cmd = tobam_cmd.format(out_file='-o %s' % tx_out_file, dext=
            'full', **locals())
    sort_opt = ''
    cores, mem = _get_cores_memory(data, downscale=4)
    splitter_cmd = tobam_cmd.format(out_file='-o %s' % tx_sr_file, dext=
        'spl', **locals())
    discordant_cmd = tobam_cmd.format(out_file='-o %s' % tx_disc_file, dext
        ='disc', **locals())
    cmd = (
        '{samblaster} --addMateTags -M --splitterFile >({splitter_cmd}) --discordantFile >({discordant_cmd}) | {dedup_cmd}'
        )
    return cmd.format(**locals())