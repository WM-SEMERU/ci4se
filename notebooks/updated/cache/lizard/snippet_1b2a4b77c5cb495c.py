def get_average(self, field=None):
    if not field:
        raise AttributeError('Please provide field to apply aggregation to!')
    agg = A('avg', field=field)
    self.aggregations['avg_' + field] = agg
    return self