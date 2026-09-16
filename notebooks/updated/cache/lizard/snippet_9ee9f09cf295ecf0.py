def aggregations(self):
    prev_month_start = get_prev_month(self.end, self.query.interval_)
    self.query.since(prev_month_start)
    self.query.get_terms('author_name')
    return self.query.get_list(dataframe=True)