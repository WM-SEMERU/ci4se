def to_data_rows(self, brains):
    fields = self.get_field_names()
    return map(lambda brain: self.get_data_record(brain, fields), brains)