def feature(self, type_=None, identifier=None, description=None, entry_name
    =None, limit=None, as_df=False):
    q = self.session.query(models.Feature)
    model_queries_config = (type_, models.Feature.type_), (identifier,
        models.Feature.identifier), (description, models.Feature.description)
    q = self.get_model_queries(q, model_queries_config)
    q = self.get_one_to_many_queries(q, ((entry_name, models.Entry.name),))
    return self._limit_and_df(q, limit, as_df)