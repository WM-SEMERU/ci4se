def Parse(self, rdf_data):
    if self._filter:
        return list(self._filter.Parse(rdf_data, self.expression))
    return rdf_data