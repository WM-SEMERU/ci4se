def write_reactions(self, stream, reactions, properties=None):
    self._write_entries(stream, reactions, self.convert_reaction_entry,
        properties)