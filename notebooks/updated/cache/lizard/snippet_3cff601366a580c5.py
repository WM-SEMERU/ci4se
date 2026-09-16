def sub_filter(self, subset, filter, inplace=True):
    full_query = ''.join(('not (', subset, ') or not (', filter, ')'))
    with LogDataChanges(self, filter_action='filter', filter_query=filter):
        result = self.data.query(full_query, inplace=inplace)
    return result