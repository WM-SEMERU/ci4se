def get_aggregated(self, attribute, category, child_limit=6, filter='',
    query='', user_query=''):
    uri = self.URI + '/aggregated?'
    uri += self.__list_or_str_to_query(attribute, 'attribute')
    uri += self.__list_or_str_to_query(category, 'category')
    uri += self.__list_or_str_to_query(child_limit, 'childLimit')
    uri += self.__list_or_str_to_query(filter, 'filter')
    uri += self.__list_or_str_to_query(query, 'query')
    uri += self.__list_or_str_to_query(user_query, 'userQuery')
    uri = uri.replace('?&', '?')
    return self._client.get(uri)