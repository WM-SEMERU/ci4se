def alternative_full_name(self, name=None, entry_name=None, limit=None,
    as_df=False):
    q = self.session.query(models.AlternativeFullName)
    model_queries_config = (name, models.AlternativeFullName.name),
    q = self.get_model_queries(q, model_queries_config)
    q = self.get_one_to_many_queries(q, ((entry_name, models.Entry.name),))
    return self._limit_and_df(q, limit, as_df)