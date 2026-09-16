def delete(adapter, case_obj, update=False, existing_case=False):
    if update:
        adapter.add_case(existing_case)
    else:
        adapter.delete_case(case_obj)
    for file_type in ['vcf_path', 'vcf_sv_path']:
        if not case_obj.get(file_type):
            continue
        variant_file = case_obj[file_type]
        vcf_obj = get_vcf(variant_file)
        delete_variants(adapter=adapter, vcf_obj=vcf_obj, case_obj=case_obj)