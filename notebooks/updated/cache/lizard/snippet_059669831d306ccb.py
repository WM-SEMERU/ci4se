def pre_script(self):
    if self['pre_script'] is None:
        return
    LOGGER.info('Executing pre script: {}'.format(self['pre_script']))
    cmd = self['pre_script']
    execute_command(self.abs_input_dir(), cmd, self.env_dictionary())
    LOGGER.info('Pre Script completed')