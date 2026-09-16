def ngram_count(self, ngram):
    query = 'SELECT count FROM _{0}_gram'.format(len(ngram))
    query += self._build_where_clause(ngram)
    query += ';'
    result = self.execute_sql(query)
    return self._extract_first_integer(result)