def _call_variants_samtools(align_bams, ref_file, items, target_regions,
    tx_out_file):
    config = items[0]['config']
    mpileup = prep_mpileup(align_bams, ref_file, config, target_regions=
        target_regions, want_bcf=True)
    bcftools = config_utils.get_program('bcftools', config)
    samtools_version = programs.get_version('samtools', config=config)
    if samtools_version and LooseVersion(samtools_version) <= LooseVersion(
        '0.1.19'):
        raise ValueError('samtools calling not supported with pre-1.0 samtools'
            )
    bcftools_opts = 'call -v -m'
    compress_cmd = '| bgzip -c' if tx_out_file.endswith('.gz') else ''
    fix_ambig_ref = vcfutils.fix_ambiguous_cl()
    fix_ambig_alt = vcfutils.fix_ambiguous_cl(5)
    cmd = (
        '{mpileup} | {bcftools} {bcftools_opts} - | {fix_ambig_ref} | {fix_ambig_alt} | vt normalize -n -q -r {ref_file} - | sed \'s/VCFv4.2/VCFv4.1/\' | sed \'s/,Version=3>/>/\' | sed \'s/,Version="3">/>/\' | sed \'s/Number=R/Number=./\' {compress_cmd} > {tx_out_file}'
        )
    do.run(cmd.format(**locals()), 'Variant calling with samtools', items[0])