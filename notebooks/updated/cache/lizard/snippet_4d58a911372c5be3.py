def rgd(self, rgdid=None, hgnc_symbol=None, hgnc_identifier=None, limit=
    None, as_df=False):
    q = self.session.query(models.RGD)
    model_queries_config = (rgdid, models.RGD.rgdid),
    q = self.get_model_queries(q, model_queries_config)
    many_to_many_queries_config = (hgnc_symbol, models.RGD.hgncs, models.
        HGNC.symbol), (hgnc_identifier, models.RGD.hgncs, models.HGNC.
        identifier)
    q = self.get_many_to_many_queries(q, many_to_many_queries_config)
    return self._limit_and_df(q, limit, as_df)