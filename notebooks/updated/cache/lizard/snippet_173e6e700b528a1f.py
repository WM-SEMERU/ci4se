def update_reading_list(self, reading_list):
    reading_list = reading_list.filter(~es_filter.Ids(values=[self.id]))
    reading_list_config = getattr(settings, 'READING_LIST_CONFIG', {})
    excluded_doc_types = reading_list_config.get('excluded_doc_types', [])
    for obj in excluded_doc_types:
        reading_list = reading_list.filter(~es_filter.Type(value=obj))
    return reading_list