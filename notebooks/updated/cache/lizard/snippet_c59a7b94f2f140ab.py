def write_compounds(self, stream, compounds, properties=None):
    self._write_entries(stream, compounds, self.convert_compound_entry,
        properties)