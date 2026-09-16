def get_project_root():
    cfg = get_project_configuration()
    for dirname in ['raw-datasets', 'preprocessed', 'feature-files',
        'models', 'reports']:
        directory = os.path.join(cfg['root'], dirname)
        if not os.path.exists(directory):
            os.makedirs(directory)
    raw_yml_path = pkg_resources.resource_filename('hwrt', 'misc/')
    raw_data_dst = os.path.join(cfg['root'], 'raw-datasets/info.yml')
    if not os.path.isfile(raw_data_dst):
        raw_yml_pkg_src = os.path.join(raw_yml_path, 'info.yml')
        shutil.copy(raw_yml_pkg_src, raw_data_dst)
    for dirname in ['models/small-baseline', 'feature-files/small-baseline',
        'preprocessed/small-baseline']:
        directory = os.path.join(cfg['root'], dirname)
        if not os.path.exists(directory):
            os.makedirs(directory)
    paths = [('preprocessed/small-baseline/',
        'preprocessing-small-info.yml'), ('feature-files/small-baseline/',
        'feature-small-info.yml'), ('models/small-baseline/',
        'model-small-info.yml')]
    for dest, src in paths:
        raw_data_dst = os.path.join(cfg['root'], '%s/info.yml' % dest)
        if not os.path.isfile(raw_data_dst):
            raw_yml_pkg_src = os.path.join(raw_yml_path, src)
            shutil.copy(raw_yml_pkg_src, raw_data_dst)
    return cfg['root']