def get_tables_for_bind(self, bind=None):
    result = []
    for table in itervalues(self.Model.metadata.tables):
        if table.info.get('bind_key') == bind:
            result.append(table)
    return result