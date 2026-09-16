def piped_bamprep(data, region=None, out_file=None):
    data['region'] = region
    if not _need_prep(data):
        return [data]
    else:
        utils.safe_makedir(os.path.dirname(out_file))
        if region[0] == 'nochrom':
            prep_bam = shared.write_nochr_reads(data['work_bam'], out_file,
                data['config'])
        elif region[0] == 'noanalysis':
            prep_bam = shared.write_noanalysis_reads(data['work_bam'],
                region[1], out_file, data['config'])
        else:
            if not utils.file_exists(out_file):
                with tx_tmpdir(data) as tmp_dir:
                    _piped_bamprep_region(data, region, out_file, tmp_dir)
            prep_bam = out_file
        bam.index(prep_bam, data['config'])
        data['work_bam'] = prep_bam
        return [data]