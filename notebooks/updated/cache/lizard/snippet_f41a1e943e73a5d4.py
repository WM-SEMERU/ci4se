def get_shared_people(self):
    people = []
    output = self._get_data()
    self._logger.debug(output)
    shared_entries = output[0] or []
    for info in shared_entries:
        try:
            people.append(Person(info))
        except InvalidData:
            self._logger.debug(
                'Missing location or other info, dropping person with info: %s'
                , info)
    return people