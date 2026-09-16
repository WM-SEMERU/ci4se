def get_help(self):
    current_state = self.get_current_state()
    if current_state is None:
        return statement(INTERNAL_ERROR_MSG)
    else:
        try:
            return choice(self._scenario_steps[current_state]['help'])
        except KeyError:
            return choice(self._default_help)