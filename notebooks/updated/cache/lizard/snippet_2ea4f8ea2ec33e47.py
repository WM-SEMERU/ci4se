def add_annotation(self, entity, annotation, value):
    url = self.base_path + 'term/add-annotation'
    data = {'tid': entity['id'], 'annotation_tid': annotation['id'],
        'value': value, 'term_version': entity['version'],
        'annotation_term_version': annotation['version']}
    return self.post(url, data)