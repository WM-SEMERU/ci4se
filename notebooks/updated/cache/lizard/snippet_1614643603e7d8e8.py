def count(self, area=None, date=None, raw=None, area_relation='Intersects',
    **keywords):
    for kw in ['order_by', 'limit', 'offset']:
        if kw in keywords:
            del keywords[kw]
    query = self.format_query(area, date, raw, area_relation, **keywords)
    _, total_count = self._load_query(query, limit=0)
    return total_count