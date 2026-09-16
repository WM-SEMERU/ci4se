def is_reading_in_require_or_assert(self, variable):
    variables_read = [n.variables_read for n in self.nodes if n.
        contains_require_or_assert()]
    variables_read = [item for sublist in variables_read for item in sublist]
    return variable in variables_read