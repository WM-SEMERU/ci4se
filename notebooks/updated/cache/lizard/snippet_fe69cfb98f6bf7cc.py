def fetch_attr_names(self, table_name):
    self.verify_table_existence(table_name)
    return self.schema_extractor.fetch_table_schema(table_name).get_attr_names(
        )