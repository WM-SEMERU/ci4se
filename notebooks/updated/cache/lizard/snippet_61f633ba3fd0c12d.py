def configure_hipchat_logger(self, hipchat_webhook=None, log_level='ERROR',
    log_format=ReportingFormats.PRETTY_PRINT.value, custom_args=''):
    hipchat_webhook = self.config.get_option('LOGGING', 'hipchat_webhook',
        None, hipchat_webhook)
    log_level = self.config.get_option('LOGGING', 'hipchat_level', None,
        log_level)
    try:
        hipchat_handler = HackyHipChatHandler(hipchat_webhook)
        self._configure_common('hipchat_', log_level, log_format, 'HipChat',
            hipchat_handler, custom_args=custom_args)
    except Exception as error_msg:
        raise error_msg