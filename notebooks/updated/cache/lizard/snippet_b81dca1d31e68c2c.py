def index(self, datastore_id=None):
    datastore = self._get_datastore_by_id(datastore_id)
    if datastore is None:
        abort(404)
    discovery_result = discover_datasources(datastore.ogrstring)
    for datasource in discovery_result:
        datasource['href'] = h.url_for(controller='datasources', action=
            'show', datastore_id=datastore_id, datasource_id=datasource['id'])
    return {'datasources': discovery_result}