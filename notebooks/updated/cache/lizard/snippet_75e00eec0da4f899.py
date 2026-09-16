def _signal_handler(self, signal_interupt, frame):
    call_file = os.path.basename(inspect.stack()[1][0].f_code.co_filename)
    call_module = inspect.stack()[1][0].f_globals['__name__'].lstrip(
        'Functions.')
    call_line = inspect.stack()[1][0].f_lineno
    self.log.error('App interrupted - file: {}, method: {}, line: {}.'.
        format(call_file, call_module, call_line))
    if signal_interupt in (2, 15):
        self.exit(1, 'The App received an interrupt signal and will now exit.')