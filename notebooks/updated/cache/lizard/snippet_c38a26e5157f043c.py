def get_meta(self, table_name, constraints=None, column_to_field_name=None,
    is_view=False, is_partition=None):
    meta = ['    class Meta(models.Model.Meta):', "        db_table = '%s'" %
        table_name]
    if self.connection.vendor == 'salesforce':
        for line in self.connection.introspection.get_additional_meta(
            table_name):
            meta.append('        ' + line)
    meta.append('')
    return meta