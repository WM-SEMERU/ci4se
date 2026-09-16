def finalize_sv(orig_vcf, data, items):
    paired = vcfutils.get_paired(items)
    if paired:
        sample_vcf = orig_vcf if paired.tumor_name == dd.get_sample_name(data
            ) else None
    else:
        sample_vcf = '%s-%s.vcf.gz' % (utils.splitext_plus(orig_vcf)[0], dd
            .get_sample_name(data))
        sample_vcf = vcfutils.select_sample(orig_vcf, dd.get_sample_name(
            data), sample_vcf, data['config'])
    if sample_vcf:
        effects_vcf, _ = effects.add_to_vcf(sample_vcf, data, 'snpeff')
    else:
        effects_vcf = None
    return effects_vcf or sample_vcf