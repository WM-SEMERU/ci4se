def _parse_asn_query(self, query_str):
    query_str_parts = self._get_query_parts(query_str)
    query_parts = list()
    for query_str_part in query_str_parts:
        is_int = True
        try:
            int(query_str_part['string'])
        except ValueError:
            is_int = False
        if is_int:
            self._logger.debug("Query part '" + query_str_part['string'] +
                "' interpreted as integer (ASN)")
            query_parts.append({'interpretation': {'string': query_str_part
                ['string'], 'interpretation': 'asn', 'attribute': 'asn',
                'operator': 'equals'}, 'operator': 'equals', 'val1': 'asn',
                'val2': query_str_part['string']})
        else:
            self._logger.debug("Query part '" + query_str_part['string'] +
                "' interpreted as text")
            query_parts.append({'interpretation': {'string': query_str_part
                ['string'], 'interpretation': 'text', 'attribute': 'name',
                'operator': 'regex'}, 'operator': 'regex_match', 'val1':
                'name', 'val2': query_str_part['string']})
    query = {}
    if len(query_parts) > 0:
        query = query_parts[0]
    if len(query_parts) > 1:
        for query_part in query_parts[1:]:
            query = {'interpretation': {'interpretation': 'and', 'operator':
                'and'}, 'operator': 'and', 'val1': query_part, 'val2': query}
    return True, query