def _get_table_counts(sheet, num_section):
    tt = sheet['table_type']
    idx_pc = sheet['idx_pc']
    idx_table = sheet['idx_table']
    idx_model = sheet['idx_model']
    if idx_pc not in num_section:
        num_section[idx_pc] = {'ct_meas': 0, 'ct_model': 0, 'ct_in_model': {}}
    try:
        if idx_model:
            if idx_model > num_section[idx_pc]['ct_model']:
                num_section[idx_pc]['ct_model'] = idx_model
            if idx_model not in num_section[idx_pc]['ct_in_model']:
                num_section[idx_pc]['ct_in_model'][idx_model] = {'ct_ens': 
                    0, 'ct_sum': 0, 'ct_dist': 0}
    except Exception as e:
        logger_excel.debug(
            'excel: get_table_counts: error incrementing model counts, '.
            format(e))
    try:
        if tt == 'measurement':
            if idx_table > num_section[idx_pc]['ct_meas']:
                num_section[idx_pc]['ct_meas'] = idx_table
        elif tt == 'distribution':
            if idx_table > num_section[idx_pc]['ct_in_model'][idx_model][
                'ct_dist']:
                num_section[idx_pc]['ct_in_model'][idx_model]['ct_dist'
                    ] = idx_table
        elif tt == 'summary':
            num_section[idx_pc]['ct_in_model'][idx_model]['ct_sum'] = 1
        elif tt == 'ensemble':
            num_section[idx_pc]['ct_in_model'][idx_model]['ct_ens'] = 1
    except Exception as e:
        logger_excel.debug(
            'excel: get_table_counts: error incrementing table count'.format(e)
            )
    return num_section