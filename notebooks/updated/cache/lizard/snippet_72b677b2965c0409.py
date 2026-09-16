def _compute_search_spaces(self, used_variables):
    return tuple(len(domain) for name, domain in self._vars.iteritems())