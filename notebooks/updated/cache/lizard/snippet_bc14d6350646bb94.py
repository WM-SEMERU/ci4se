def get_select_sql(self):
    return '{0}({1}{2}){3}'.format(self.name.upper(), self.get_distinct(),
        self.get_field_identifier(), self.get_over())