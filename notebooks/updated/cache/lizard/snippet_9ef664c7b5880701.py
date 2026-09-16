async def prefetch(self, query, *subqueries):
    query = self._swap_database(query)
    subqueries = map(self._swap_database, subqueries)
    return await prefetch(query, *subqueries)