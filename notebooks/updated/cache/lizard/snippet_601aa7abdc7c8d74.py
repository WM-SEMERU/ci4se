def django_table_names(self, only_existing=False, **kwargs):
    all_models = list(chain.from_iterable(self.cql_models.values()))
    tables = [model.column_family_name(include_keyspace=False) for model in
        all_models]
    return tables