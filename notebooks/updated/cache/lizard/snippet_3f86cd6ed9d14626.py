def stream(self, date_created_after=values.unset, date_created_before=
    values.unset, track=values.unset, publisher=values.unset, kind=values.
    unset, limit=None, page_size=None):
    limits = self._version.read_limits(limit, page_size)
    page = self.page(date_created_after=date_created_after,
        date_created_before=date_created_before, track=track, publisher=
        publisher, kind=kind, page_size=limits['page_size'])
    return self._version.stream(page, limits['limit'], limits['page_limit'])