def _get_maxcov_downsample(data):
    from bcbio.bam import ref
    from bcbio.ngsalign import alignprep, bwa
    from bcbio.variation import coverage
    fastq_file = data['files'][0]
    params = alignprep.get_downsample_params(data)
    if params:
        num_reads = alignprep.total_reads_from_grabix(fastq_file)
        if num_reads:
            vrs = dd.get_variant_regions_merged(data)
            total_size = sum([c.size for c in ref.file_contigs(dd.
                get_ref_file(data), data['config'])])
            if vrs:
                callable_size = pybedtools.BedTool(vrs).total_coverage()
                genome_cov_pct = callable_size / float(total_size)
            else:
                callable_size = total_size
                genome_cov_pct = 1.0
            if (genome_cov_pct > coverage.GENOME_COV_THRESH and dd.
                get_coverage_interval(data) in ['genome', None, False]):
                total_counts, total_sizes = 0, 0
                for count, size in bwa.fastq_size_output(fastq_file, 5000):
                    total_counts += int(count)
                    total_sizes += int(size) * int(count)
                read_size = float(total_sizes) / float(total_counts)
                avg_cov = float(num_reads * read_size) / callable_size
                if avg_cov >= params['min_coverage_for_downsampling']:
                    return int(avg_cov * params['maxcov_downsample_multiplier']
                        )
    return None