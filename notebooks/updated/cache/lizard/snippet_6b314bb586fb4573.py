def delete(self, query):
    record = self.get(query=query).one()
    self._url = self._url_builder.get_appended_custom('/{0}'.format(record[
        'sys_id']))
    return self._get_response('DELETE').one()