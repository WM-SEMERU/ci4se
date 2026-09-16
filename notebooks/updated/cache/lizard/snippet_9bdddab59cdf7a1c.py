def run_command(self, config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    rdbms = config.get('database', 'rdbms').lower()
    wrapper = self.create_routine_wrapper_generator(rdbms)
    wrapper.main(config_file)