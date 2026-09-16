def find_cached_dm(self):
    pmag_dir = find_pmag_dir.get_pmag_dir()
    if pmag_dir is None:
        pmag_dir = '.'
    model_file = os.path.join(pmag_dir, 'pmagpy', 'data_model',
        'data_model.json')
    if not os.path.isfile(model_file):
        model_file = os.path.join(pmag_dir, 'data_model', 'data_model.json')
    if not os.path.isfile(model_file):
        model_file = os.path.join(os.path.split(os.path.dirname(__file__))[
            0], 'pmagpy', 'data_model', 'data_model.json')
    if not os.path.isfile(model_file):
        model_file = os.path.join(os.path.split(os.path.dirname(__file__))[
            0], 'data_model', 'data_model.json')
    return model_file