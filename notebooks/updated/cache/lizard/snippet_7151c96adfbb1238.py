def log_error(self, message, *args, **kwargs):
    self._service.log(logging.ERROR, message, *args, **kwargs)