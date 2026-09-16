def get_runs(self, sort_by=None, sort_direction=None, start=0, limit=None,
    query={'type': 'and', 'filters': []}):
    mongo_query = self._to_mongo_query(query)
    r = self.generic_dao.find_records(self.collection_name, mongo_query,
        sort_by, sort_direction, start, limit)
    return r