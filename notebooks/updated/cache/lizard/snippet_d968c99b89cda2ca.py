def get_aggregation(self, name):
    agg = self.aggregations[name]
    if 'buckets' in agg:
        return agg['buckets']
    else:
        return agg