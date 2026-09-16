def load_config(filename, config_dir=None, copy_default_config=True):
    if not config_dir:
        config_file = os.path.join(get_default_config_path(), filename)
    else:
        config_file = os.path.join(config_dir, filename)
        if not os.path.isfile(config_file):
            if copy_default_config:
                logger.info(
                    'Config file {} not found, I will create a default version'
                    .format(config_file))
                make_directory(config_dir)
                shutil.copy(os.path.join(package_path, 'config', filename.
                    replace('.cfg', '_default.cfg')), config_file)
            else:
                message = 'Config file {} not found.'.format(config_file)
                logger.error(message)
                raise FileNotFoundError(message)
    if len(cfg.read(config_file)) == 0:
        message = 'Config file {} not found or empty.'.format(config_file)
        logger.error(message)
        raise FileNotFoundError(message)
    global _loaded
    _loaded = True