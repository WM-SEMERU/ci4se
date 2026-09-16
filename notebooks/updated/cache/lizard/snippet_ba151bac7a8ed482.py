def filters_apply(self, objects, filters, context):
    filter_strings = []
    for keyword_filter in filters:
        if not context in keyword_filter['context']:
            continue
        filter_string = re.escape(keyword_filter['phrase'])
        if keyword_filter['whole_word'] == True:
            filter_string = '\\b' + filter_string + '\\b'
        filter_strings.append(filter_string)
    filter_re = re.compile('|'.join(filter_strings), flags=re.IGNORECASE)
    filter_results = []
    for filter_object in objects:
        filter_status = filter_object
        if 'status' in filter_object:
            filter_status = filter_object['status']
        filter_text = filter_status['content']
        filter_text = re.sub('<.*?>', ' ', filter_text)
        filter_text = re.sub('\\s+', ' ', filter_text).strip()
        if not filter_re.search(filter_text):
            filter_results.append(filter_object)
    return filter_results