def get_applicable_values(self):
    return [v for v in self._values if v.is_active and not v.is_all_results]