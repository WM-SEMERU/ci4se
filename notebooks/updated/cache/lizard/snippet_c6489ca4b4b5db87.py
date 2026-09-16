def unlink_intermediate(self, sourceId, targetId):
    source = self.database['items'][self.database.get('name'), sourceId]
    target = self.database['items'][self.database.get('name'), targetId]
    production_exchange = [x['input'] for x in source['exchanges'] if x[
        'type'] == 'production'][0]
    new_exchanges = [x for x in target['exchanges'] if x['input'] !=
        production_exchange]
    target['exchanges'] = new_exchanges
    self.parameter_scan()
    return True