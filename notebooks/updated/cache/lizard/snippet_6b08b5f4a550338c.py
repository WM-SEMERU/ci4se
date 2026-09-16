def update_person(self, person):
    self._validate_regid(person.person_id)
    self._validate_subscriber_id(person.surrogate_id)
    for attr in MANAGED_ATTRIBUTES:
        person.attributes.pop(attr, None)
    url = '/notification/v1/person/{}'.format(person.person_id)
    response = NWS_DAO().putURL(url, self._write_headers(), self._json_body
        (person.json_data()))
    if response.status != 204:
        raise DataFailureException(url, response.status, response.data)
    return response.status