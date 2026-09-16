def stream(self, actor_sid=values.unset, event_type=values.unset,
    resource_sid=values.unset, source_ip_address=values.unset, start_date=
    values.unset, end_date=values.unset, limit=None, page_size=None):
    limits = self._version.read_limits(limit, page_size)
    page = self.page(actor_sid=actor_sid, event_type=event_type,
        resource_sid=resource_sid, source_ip_address=source_ip_address,
        start_date=start_date, end_date=end_date, page_size=limits['page_size']
        )
    return self._version.stream(page, limits['limit'], limits['page_limit'])