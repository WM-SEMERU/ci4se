def _get_paths():
    import os
    base_path = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.join(base_path, 'tests', 'data', 'Plate01')
    test_data_file = os.path.join(test_data_dir, 'RFP_Well_A3.fcs')
    return test_data_dir, test_data_file