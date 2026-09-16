def health_check(self):
    logger.debug('Health Check on file for: {namespace}'.format(namespace=
        self.namespace))
    return os.path.isfile(self.data_file)