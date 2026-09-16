def get_attributes(self, no_cache=False):
    if not self.attributes:
        self.ldap_connection.search(search_base=self.ATTRIBUTES_SEARCH[
            'base_dn'], search_filter=self.ATTRIBUTES_SEARCH[
            'filter_string'], search_scope=self.ATTRIBUTES_SEARCH['scope'],
            attributes=self.ATTRIBUTES_SEARCH['attribute_list'])
        results = [result['attributes'] for result in self.ldap_connection.
            response if result['type'] == 'searchResEntry']
        if len(results) != 1:
            logger.debug('Search returned {count} results: {results}'.
                format(count=len(results), results=results))
        if results:
            self.attributes = results[0]
        else:
            self.attributes = []
    return self.attributes