def fetch_one(self, *args, **kwargs):
    bson_obj = self.fetch(*args, **kwargs)
    count = bson_obj.count()
    if count > 1:
        raise MultipleResultsFound('%s results found' % count)
    elif count == 1:
        return next(bson_obj)