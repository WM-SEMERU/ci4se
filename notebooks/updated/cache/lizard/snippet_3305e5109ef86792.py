def clean(self):
    if self.config.clean:
        logger.info('Cleaning')
        self.execute(self.config.clean)