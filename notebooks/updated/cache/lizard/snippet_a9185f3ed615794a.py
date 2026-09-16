def list(self, from_=values.unset, to=values.unset,
    date_created_on_or_before=values.unset, date_created_after=values.unset,
    limit=None, page_size=None):
    return list(self.stream(from_=from_, to=to, date_created_on_or_before=
        date_created_on_or_before, date_created_after=date_created_after,
        limit=limit, page_size=page_size))