def _expand_alts_in_vcf_record_list(cls, vcf_records):
    new_vcf_records = []
    for record in vcf_records:
        new_vcf_records.extend(record.to_record_per_alt())
    return new_vcf_records