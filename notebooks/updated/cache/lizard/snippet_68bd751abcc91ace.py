def setup_logging(self):
    is_custom_logging = len(self.options.logging_config) > 0
    is_custom_logging = is_custom_logging and os.path.isfile(self.options.
        logging_config)
    is_custom_logging = is_custom_logging and not self.options.dry_run
    if is_custom_logging:
        Logger.configure_by_file(self.options.logging_config)
    else:
        logging_format = '%(asctime)-15s - %(name)s - %(message)s'
        if self.options.dry_run:
            logging_format = '%(name)s - %(message)s'
        Logger.configure_default(logging_format, self.logging_level)