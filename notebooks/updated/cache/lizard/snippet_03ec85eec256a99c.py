def get_field_cache(self, cache_type='es'):
    if cache_type == 'kibana':
        try:
            search_results = urlopen(self.get_url).read().decode('utf-8')
        except HTTPError:
            return []
        index_pattern = json.loads(search_results)
        fields_str = index_pattern['_source']['fields']
        return json.loads(fields_str)
    elif cache_type == 'es' or cache_type.startswith('elastic'):
        search_results = urlopen(self.es_get_url).read().decode('utf-8')
        es_mappings = json.loads(search_results)
        field_cache = []
        for index_name, val in iteritems(es_mappings):
            if index_name != self.index:
                m_dict = es_mappings[index_name]['mappings']
                mappings = self.get_index_mappings(m_dict)
                field_cache.extend(mappings)
        field_cache = self.dedup_field_cache(field_cache)
        return field_cache
    self.pr_err('Unknown cache type: %s' % cache_type)
    return None