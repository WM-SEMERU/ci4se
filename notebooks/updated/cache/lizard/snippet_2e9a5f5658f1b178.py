def get_received_events(self):
    return github.PaginatedList.PaginatedList(github.Event.Event, self.
        _requester, self.url + '/received_events', None)