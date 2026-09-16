def run_steps_from_string(self, spec, language_name='en'):
    caller = inspect.currentframe().f_back
    line = caller.f_lineno - 1
    fname = caller.f_code.co_filename
    steps = parse_steps(spec, fname, line, load_language(language_name))
    for s in steps:
        self.run_step(s)