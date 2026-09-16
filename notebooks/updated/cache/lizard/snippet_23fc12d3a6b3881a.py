def _name_to_index(self, cursor, table_name):
    return dict([(d[0], i) for i, d in enumerate(self.get_table_description
        (cursor, table_name, identity_check=False))])