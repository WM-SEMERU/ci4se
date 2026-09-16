def delete_report(self, report_id, id_type=None):
    params = {'idType': id_type}
    self._client.delete('reports/%s' % report_id, params=params)