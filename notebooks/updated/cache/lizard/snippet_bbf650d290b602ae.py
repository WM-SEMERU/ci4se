def purge(self, doc_ids):
    title = '%s.purge' % self.__class__.__name__
    if isinstance(doc_ids, str):
        doc_ids = [doc_ids]
    input_fields = {'doc_ids': doc_ids}
    for key, value in input_fields.items():
        object_title = '%s(%s=%s)' % (title, key, str(value))
        self.fields.validate(value, '.%s' % key, object_title)
    url = self.bucket_url + '/_purge'
    json_body = {}
    for doc in doc_ids:
        json_body[doc] = ['*']
    response = requests.post(url, json=json_body)
    purged_list = []
    purged_map = {}
    response_details = response.json()
    if 'purged' in response_details.keys():
        purged_map = response_details['purged']
    for key in purged_map.keys():
        purged_list.append(key)
    return purged_list