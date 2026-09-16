def setup_alignak_logger(self):
    try:
        self.check_dir(self.logdir)
        setup_logger(logger_configuration_file=self.logger_configuration,
            log_dir=self.logdir, process_name=self.name, log_file=self.
            log_filename)
        if self.debug:
            set_log_level('DEBUG')
            logger.info('-----')
            logger.info('Daemon log level set to a minimum of DEBUG')
            logger.info('-----')
        elif self.verbose:
            set_log_level('INFO')
            logger.info('-----')
            logger.info('Daemon log level set to a minimum of INFO')
            logger.info('-----')
        elif self.log_level:
            set_log_level(self.log_level)
            logger.info('-----')
            logger.info('Daemon log level set to %s', self.log_level)
            logger.info('-----')
    except Exception as exp:
        print('***** %s - exception when setting-up the logger: %s' % (self
            .name, exp))
        self.exit_on_exception(exp, message='Logger configuration error!')
    logger.debug('Alignak daemon logger configured')
    for line in self.get_header():
        logger.info('- %s', line)
    for line in self.get_header(configuration=True):
        logger.debug('- %s', line)
    if self.pre_log:
        logger.debug('--- Start - Log prior to our configuration:')
        for level, message in self.pre_log:
            fun_level = level.lower()
            getattr(logger, fun_level)('- %s', message)
        logger.debug('--- Stop - Log prior to our configuration')