def new_calendar(self, calendar_name):
    if not calendar_name:
        return None
    url = self.build_url(self._endpoints.get('root_calendars'))
    response = self.con.post(url, data={self._cc('name'): calendar_name})
    if not response:
        return None
    data = response.json()
    return self.calendar_constructor(parent=self, **{self._cloud_data_key:
        data})