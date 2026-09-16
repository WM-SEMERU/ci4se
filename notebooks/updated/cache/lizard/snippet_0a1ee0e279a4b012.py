def set_name_with_model(self, model):
    table_name = model._meta.db_table
    column_names = [model._meta.get_field(field_name).column for field_name,
        order in self.fields_orders]
    column_names_with_order = [(('-%s' if order else '%s') % column_name) for
        column_name, (field_name, order) in zip(column_names, self.
        fields_orders)]
    hash_data = [table_name] + column_names_with_order + [self.suffix
        ] + self.name_hash_extra_data()
    self.name = '%s_%s_%s' % (table_name[:11], column_names[0][:7], '%s_%s' %
        (self._hash_generator(*hash_data), self.suffix))
    assert len(self.name
        ) <= self.max_name_length, 'Index too long for multiple database support. Is self.suffix longer than 3 characters?'
    self.check_name()