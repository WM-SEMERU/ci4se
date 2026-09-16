def get(self, id, **options):
    if not self._item_path:
        raise AttributeError('get is not available for %s' % self._item_name)
    target = self._item_path % id
    json_data = self._redmine.get(target, **options)
    data = self._redmine.unwrap_json(self._item_type, json_data)
    data['_source_path'] = target
    return self._objectify(data=data)