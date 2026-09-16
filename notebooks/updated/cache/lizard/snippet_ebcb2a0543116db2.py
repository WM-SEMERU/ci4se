def _bgzip_from_cram_sambamba(cram_file, dirs, data):
    raise NotImplementedError(
        "sambamba doesn't yet support retrieval from CRAM by BED file")
    region_file = tz.get_in(['config', 'algorithm', 'variant_regions'], data
        ) if tz.get_in(['config', 'algorithm', 'coverage_interval'], data) in [
        'regional', 'exome'] else None
    base_name = utils.splitext_plus(os.path.basename(cram_file))[0]
    work_dir = utils.safe_makedir(os.path.join(dirs['work'], 'align_prep', 
        '%s-parts' % base_name))
    f1, f2, o1, o2, si = [os.path.join(work_dir, '%s.fq' % x) for x in [
        'match1', 'match2', 'unmatch1', 'unmatch2', 'single']]
    ref_file = dd.get_ref_file(data)
    region = '-L %s' % region_file if region_file else ''
    cmd = (
        'sambamba view -f bam -l 0 -C {cram_file} -T {ref_file} {region} | bamtofastq F={f1} F2={f2} S={si} O={o1} O2={o2}'
        )
    do.run(cmd.format(**locals()), 'Convert CRAM to fastq in regions')