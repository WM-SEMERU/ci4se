def _do_run(paired):
    work_dir = _sv_workdir(paired.tumor_data)
    out = _get_battenberg_out(paired, work_dir)
    ignore_file = os.path.join(work_dir, 'ignore_chromosomes.txt')
    if len(_missing_files(out)) > 0:
        ref_file = dd.get_ref_file(paired.tumor_data)
        bat_datadir = os.path.normpath(os.path.join(os.path.dirname(
            ref_file), os.pardir, 'battenberg'))
        ignore_file, gl_file = _make_ignore_file(work_dir, ref_file,
            ignore_file, os.path.join(bat_datadir, 'impute', 'impute_info.txt')
            )
        tumor_bam = paired.tumor_bam
        normal_bam = paired.normal_bam
        platform = dd.get_platform(paired.tumor_data)
        genome_build = paired.tumor_data['genome_build']
        cores = max(1, int(dd.get_num_cores(paired.tumor_data) * 0.5))
        gender = {'male': 'XY', 'female': 'XX', 'unknown': 'L'}.get(population
            .get_gender(paired.tumor_data))
        if gender == 'L':
            gender_str = '-ge %s -gl %s' % (gender, gl_file)
        else:
            gender_str = '-ge %s' % gender
        r_export_cmd = utils.get_R_exports()
        local_sitelib = utils.R_sitelib()
        cmd = (
            'export R_LIBS_USER={local_sitelib} && {r_export_cmd} && battenberg.pl -t {cores} -o {work_dir} -r {ref_file}.fai -tb {tumor_bam} -nb {normal_bam} -e {bat_datadir}/impute/impute_info.txt -u {bat_datadir}/1000genomesloci -c {bat_datadir}/probloci.txt -ig {ignore_file} {gender_str} -assembly {genome_build} -species Human -platform {platform}'
            )
        do.run(cmd.format(**locals()), 'Battenberg CNV calling')
    assert len(_missing_files(out)
        ) == 0, 'Missing Battenberg output: %s' % _missing_files(out)
    out['plot'] = _get_battenberg_out_plots(paired, work_dir)
    out['ignore'] = ignore_file
    return out