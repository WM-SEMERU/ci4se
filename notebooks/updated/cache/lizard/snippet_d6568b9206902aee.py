def derive_data(data):
    for s_name, values in data.items():
        total_called_variants = 0
        for value_name in ['TOTAL_SNPS', 'TOTAL_COMPLEX_INDELS',
            'TOTAL_MULTIALLELIC_SNPS', 'TOTAL_INDELS']:
            total_called_variants = total_called_variants + int(values[
                value_name])
        values['total_called_variants'] = total_called_variants
        total_called_variants_known = 0
        for value_name in ['NUM_IN_DB_SNP', 'NUM_IN_DB_SNP_COMPLEX_INDELS',
            'NUM_IN_DB_SNP_MULTIALLELIC']:
            total_called_variants_known = total_called_variants_known + int(
                values[value_name])
        total_called_variants_known = total_called_variants_known + int(values
            ['TOTAL_INDELS']) - int(values['NOVEL_INDELS'])
        values['total_called_variants_known'] = total_called_variants_known
        values['total_called_variants_novel'
            ] = total_called_variants - total_called_variants_known