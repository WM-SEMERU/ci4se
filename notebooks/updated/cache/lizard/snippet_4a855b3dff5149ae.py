def get_event(self, id):
    url = '%s/%s' % (Event.resource_url(), id)
    response = json.loads(self._call(url).text)
    return EventDataWrapper(self, response)