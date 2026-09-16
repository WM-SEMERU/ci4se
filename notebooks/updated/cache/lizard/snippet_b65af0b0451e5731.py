def setup_dryx_logging(yaml_file):
    import logging
    import logging.config
    import yaml
    handlers.GroupWriteRotatingFileHandler = GroupWriteRotatingFileHandler
    stream = file(yaml_file, 'r')
    yamlContent = yaml.load(stream)
    stream.close()
    if 'logging settings' in yamlContent:
        yamlContent = yamlContent['logging settings']
        yamlContent['version'] = 1
    logging.config.dictConfig(yamlContent)
    logger = logging.getLogger(__name__)
    logging.captureWarnings(True)
    return logger