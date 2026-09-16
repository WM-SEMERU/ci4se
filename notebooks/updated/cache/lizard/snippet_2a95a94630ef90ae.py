def where(self, custom_restrictions=[], **restrictions):
    standard_names, standard_values = self._standard_items(restrictions)
    custom_names, custom_values = self._custom_items(custom_restrictions)
    in_names, in_values = self._in_items(restrictions)
    query_names = standard_names + custom_names + in_names
    if query_names:
        self.where_values = standard_values + custom_values + in_values
        self.where_clause = 'where {query} '.format(query=' and '.join(
            query_names))
    return self