def search(self, search_phrase, limit=None):
    search_phrase = search_phrase.replace('-', '_')
    terms = SearchTermParser().parse(search_phrase)
    from_year = terms.pop('from', None)
    to_year = terms.pop('to', None)
    query, query_params = self._make_query_from_terms(terms)
    self._parsed_query = query, query_params
    connection = self.backend.library.database.connection
    connection.connection.create_function('rank', 1, _make_rank_func((1.0, 
        0.1, 0, 0)))
    results = connection.execute(query, query_params).fetchall()
    for result in results:
        vid, dataset_vid, score, db_from_year, db_to_year = result
        if from_year and from_year < db_from_year:
            continue
        if to_year and to_year > db_to_year:
            continue
        yield PartitionSearchResult(vid=vid, dataset_vid=dataset_vid, score
            =score)