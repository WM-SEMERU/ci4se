def download(url):
    filepath = get_file(fname='tmp.zip', origin=url, extract=True)
    base_dir = os.path.dirname(filepath)
    weights_file = os.path.join(base_dir, 'weights.h5')
    params_file = os.path.join(base_dir, 'params.json')
    preprocessor_file = os.path.join(base_dir, 'preprocessor.pickle')
    return weights_file, params_file, preprocessor_file