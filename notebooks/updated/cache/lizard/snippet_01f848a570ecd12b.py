def _get_full_paths(fastq_dir, config, config_file):
    if fastq_dir:
        fastq_dir = utils.add_full_path(fastq_dir)
    config_dir = utils.add_full_path(os.path.dirname(config_file))
    galaxy_config_file = utils.add_full_path(config.get('galaxy_config',
        'universe_wsgi.ini'), config_dir)
    return fastq_dir, os.path.dirname(galaxy_config_file), config_dir