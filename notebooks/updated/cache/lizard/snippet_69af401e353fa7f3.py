def _get_date_pagination(self, base, oldest_neighbor, newest_neighbor):
    _, span, date_format = utils.parse_date(self.spec['date'])
    if newest_neighbor:
        newer_date = newest_neighbor.date.span(span)[0]
        newer_view = View({**base, 'order': self._order_by, 'date':
            newer_date.format(date_format)})
    else:
        newer_view = None
    if oldest_neighbor:
        older_date = oldest_neighbor.date.span(span)[0]
        older_view = View({**base, 'order': self._order_by, 'date':
            older_date.format(date_format)})
    else:
        older_view = None
    return older_view, newer_view