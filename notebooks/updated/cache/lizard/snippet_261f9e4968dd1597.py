def get_ccle_mrna(gene_list, cell_lines):
    gene_list_str = ','.join(gene_list)
    data = {'cmd': 'getProfileData', 'case_set_id': ccle_study + '_mrna',
        'genetic_profile_id': ccle_study + '_mrna', 'gene_list':
        gene_list_str, 'skiprows': -1}
    df = send_request(**data)
    mrna_amounts = {cl: {g: [] for g in gene_list} for cl in cell_lines}
    for cell_line in cell_lines:
        if cell_line in df.columns:
            for gene in gene_list:
                value_cell = df[cell_line][df['COMMON'] == gene]
                if value_cell.empty:
                    mrna_amounts[cell_line][gene] = None
                elif pandas.isnull(value_cell.values[0]):
                    mrna_amounts[cell_line][gene] = None
                else:
                    value = value_cell.values[0]
                    mrna_amounts[cell_line][gene] = value
        else:
            mrna_amounts[cell_line] = None
    return mrna_amounts