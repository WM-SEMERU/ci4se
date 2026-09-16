def features_of_type(self, featuretype, limit=None, strand=None, order_by=
    None, reverse=False, completely_within=False):
    query, args = helpers.make_query(args=[], limit=limit, featuretype=
        featuretype, order_by=order_by, reverse=reverse, strand=strand,
        completely_within=completely_within)
    for i in self._execute(query, args):
        yield self._feature_returner(**i)