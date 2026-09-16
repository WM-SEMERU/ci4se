def _get_user_dn(self, user_lookup_attribute_value):
    self.ldap_connection.search(search_base=self.USER_SEARCH['base_dn'],
        search_filter=self.USER_SEARCH['filter_string'].format(lookup_value
        =escape_query(user_lookup_attribute_value)), search_scope=self.
        USER_SEARCH['scope'], attributes=self.USER_SEARCH['attribute_list'])
    results = [result['dn'] for result in self.ldap_connection.response if 
        result['type'] == 'searchResEntry']
    if not results:
        raise AccountDoesNotExist(
            'The {user_lookup_attribute} provided does not exist in the Active Directory.'
            .format(user_lookup_attribute=self.user_lookup_attr))
    if len(results) > 1:
        logger.debug('Search returned more than one result: {results}'.
            format(results=results))
    if results:
        return results[0]
    else:
        return results