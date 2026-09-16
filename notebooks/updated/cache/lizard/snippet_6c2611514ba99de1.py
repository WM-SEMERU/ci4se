def part_search(self, part_query):
    limit = 100
    results = self._e.parts_search(q=part_query, limit=limit)
    start = 0
    hits = results[0]['hits']
    if hits == 0:
        print('No result')
        return ReturnValues.NO_RESULTS
    print("Searched for: '{}'".format(results[0]['request']['q']))

    def show_result(r):
        print(' → {:30} {:30} {}'.format(r['item']['mpn'], r['item'][
            'manufacturer']['name'], r['snippet']))
    for r in results[1]:
        show_result(r)
    while hits - limit > limit:
        start += limit
        hits -= limit
        results = self._e.parts_search(q=part_query, limit=limit, start=start)
        for r in results[1]:
            show_result(r)
    if hits - limit > 0:
        start += limit
        hits -= limit
        results = self._e.parts_search(q=part_query, limit=hits, start=start)
        for r in results[1]:
            show_result(r)
    return ReturnValues.OK