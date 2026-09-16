def write_noanalysis_reads(in_file, region_file, out_file, config):
    if not file_exists(out_file):
        with file_transaction(config, out_file) as tx_out_file:
            bedtools = config_utils.get_program('bedtools', config)
            sambamba = config_utils.get_program('sambamba', config)
            cl = (
                '{sambamba} view -f bam -l 0 -L {region_file} {in_file} | {bedtools} intersect -abam - -b {region_file} -f 1.0 -nonamecheck> {tx_out_file}'
                )
            do.run(cl.format(**locals()), 'Select unanalyzed reads')
    return out_file