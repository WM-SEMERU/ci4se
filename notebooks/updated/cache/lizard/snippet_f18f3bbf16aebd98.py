def return_handler(module_logger, first_is_session=True):

    def _outer(visa_library_method):

        def _inner(self, session, *args, **kwargs):
            ret_value = visa_library_method(*args, **kwargs)
            module_logger.debug('%s%s -> %r', visa_library_method.__name__,
                _args_to_str(args, kwargs), ret_value)
            try:
                ret_value = constants.StatusCode(ret_value)
            except ValueError:
                pass
            if first_is_session:
                self._last_status = ret_value
                self._last_status_in_session[session] = ret_value
            if ret_value < 0:
                raise VisaIOError(ret_value)
            if ret_value in self.issue_warning_on:
                if (session and ret_value not in self.
                    _ignore_warning_in_session[session]):
                    module_logger.warn(VisaIOWarning(ret_value), stacklevel=2)
            return ret_value
        return _inner
    return _outer