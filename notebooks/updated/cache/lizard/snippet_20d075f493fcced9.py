def get_definition(self):
    match = self._bracket_exact_var(self.context.exact_match)
    if match is None:
        match = self._bracket_exact_exec(self.context.exact_match)
    return match