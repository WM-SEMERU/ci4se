def get_cancer_types(cancer_filter=None):
    data = {'cmd': 'getTypesOfCancer'}
    df = send_request(**data)
    res = _filter_data_frame(df, ['type_of_cancer_id'], 'name', cancer_filter)
    type_ids = list(res['type_of_cancer_id'].values())
    return type_ids