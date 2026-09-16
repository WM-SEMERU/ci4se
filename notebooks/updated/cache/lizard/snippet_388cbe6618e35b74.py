def update_config(file_name, yaml_contents):
    file_name = '{0}{1}'.format(file_name, '.conf')
    dir_path = os.path.join(__opts__['config_dir'], os.path.dirname(
        __opts__['default_include']))
    try:
        yaml_out = salt.utils.yaml.safe_dump(yaml_contents,
            default_flow_style=False)
        if not os.path.exists(dir_path):
            log.debug('Creating directory %s', dir_path)
            os.makedirs(dir_path, 493)
        file_path = os.path.join(dir_path, file_name)
        with salt.utils.files.fopen(file_path, 'w') as fp_:
            fp_.write(yaml_out)
        return 'Wrote {0}'.format(file_name)
    except (IOError, OSError, salt.utils.yaml.YAMLError, ValueError) as err:
        return six.text_type(err)