def configure_logger(self, tc_config_log_filename=None,
    tc_output_log_filename=None):
    config_log_filename = DriverWrappersPool.get_configured_value(
        'Config_log_filename', tc_config_log_filename, 'logging.conf')
    config_log_filename = os.path.join(DriverWrappersPool.config_directory,
        config_log_filename)
    if self.config_log_filename != config_log_filename:
        output_log_filename = DriverWrappersPool.get_configured_value(
            'Output_log_filename', tc_output_log_filename, 'toolium.log')
        output_log_filename = os.path.join(DriverWrappersPool.
            output_directory, output_log_filename)
        output_log_filename = output_log_filename.replace('\\', '\\\\')
        try:
            logging.config.fileConfig(config_log_filename, {'logfilename':
                output_log_filename}, False)
        except Exception as exc:
            print("[WARN] Error reading logging config file '{}': {}".
                format(config_log_filename, exc))
        self.config_log_filename = config_log_filename
        self.output_log_filename = output_log_filename
        self.logger = logging.getLogger(__name__)