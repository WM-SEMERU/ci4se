def events(self, start_time, include=None):
    return self._query_zendesk(self.endpoint.events, 'ticket_event',
        start_time=start_time, include=include)