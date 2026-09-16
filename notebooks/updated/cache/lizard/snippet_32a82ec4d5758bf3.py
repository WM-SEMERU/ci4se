def metta_config(quarter, num_dimensions):
    first_day, last_day = quarter_boundaries(quarter)
    return {'start_time': first_day, 'end_time': last_day,
        'prediction_window': 3, 'label_name': 'onet_soc_code', 'label_type':
        'categorical', 'matrix_id': 'job_postings_{}'.format(quarter),
        'feature_names': ['doc2vec_{}'.format(i) for i in range(
        num_dimensions)]}