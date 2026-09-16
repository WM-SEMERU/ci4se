def validate_customized_file(experiment_config, spec_key):
    if experiment_config[spec_key].get('codeDir') and experiment_config[
        spec_key].get('classFileName') and experiment_config[spec_key].get(
        'className'):
        if not os.path.exists(os.path.join(experiment_config[spec_key][
            'codeDir'], experiment_config[spec_key]['classFileName'])):
            print_error('%s file directory is not valid!' % spec_key)
            exit(1)
    else:
        print_error('%s file directory is not valid!' % spec_key)
        exit(1)