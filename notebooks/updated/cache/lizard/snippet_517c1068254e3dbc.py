def get_entity_by_netid(self, netid):
    if not self.valid_uwnetid(netid):
        raise InvalidNetID(netid)
    url = '{}/{}.json'.format(ENTITY_PREFIX, netid.lower())
    response = DAO.getURL(url, {'Accept': 'application/json'})
    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)
    return self._entity_from_json(response.data)