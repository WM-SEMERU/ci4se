def prep_hla(work_dir, sample, calls, hlas, normal_bam, tumor_bam):
    work_dir = utils.safe_makedir(os.path.join(work_dir, sample, 'inputs'))
    hla_file = os.path.join(work_dir, '%s-hlas.txt' % sample)
    with open(calls) as in_handle:
        with open(hla_file, 'w') as out_handle:
            next(in_handle)
            for line in in_handle:
                _, _, a, _, _ = line.strip().split(',')
                a1, a2 = a.split(';')
                out_handle.write(get_hla_choice(name_to_absolute(a1), hlas,
                    normal_bam, tumor_bam) + '\n')
                out_handle.write(get_hla_choice(name_to_absolute(a2), hlas,
                    normal_bam, tumor_bam) + '\n')
    return hla_file