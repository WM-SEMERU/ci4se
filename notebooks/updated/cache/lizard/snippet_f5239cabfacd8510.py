def load_train_file(config_file_path):
    from pylearn2.config import yaml_parse
    suffix_to_strip = '.yaml'
    if config_file_path.endswith(suffix_to_strip):
        config_file_full_stem = config_file_path[0:-len(suffix_to_strip)]
    else:
        config_file_full_stem = config_file_path
    for varname in ['PYLEARN2_TRAIN_FILE_NAME', 'PYLEARN2_TRAIN_FILE_FULL_STEM'
        ]:
        environ.putenv(varname, config_file_full_stem)
    directory = config_file_path.split('/')[:-1]
    directory = '/'.join(directory)
    if directory != '':
        directory += '/'
    environ.putenv('PYLEARN2_TRAIN_DIR', directory)
    environ.putenv('PYLEARN2_TRAIN_BASE_NAME', config_file_path.split('/')[-1])
    environ.putenv('PYLEARN2_TRAIN_FILE_STEM', config_file_full_stem.split(
        '/')[-1])
    return yaml_parse.load_path(config_file_path)