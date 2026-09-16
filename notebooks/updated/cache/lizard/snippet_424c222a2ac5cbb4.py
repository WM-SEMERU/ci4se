def get_alias(self):
    alias = None
    if self.alias:
        alias = self.alias
    elif self.auto_alias:
        alias = self.auto_alias
    if self.table and self.table.prefix_fields:
        field_prefix = self.table.get_field_prefix()
        if alias:
            alias = '{0}__{1}'.format(field_prefix, alias)
        else:
            alias = '{0}__{1}'.format(field_prefix, self.name)
    return alias