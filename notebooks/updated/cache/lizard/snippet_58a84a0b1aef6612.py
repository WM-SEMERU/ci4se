def get_calendar(self, listing_id, starting_month=datetime.datetime.now().
    month, starting_year=datetime.datetime.now().year, calendar_months=12):
    params = {'year': str(starting_year), 'listing_id': str(listing_id),
        '_format': 'with_conditions', 'count': str(calendar_months),
        'month': str(starting_month)}
    r = self._session.get(API_URL + '/calendar_months', params=params)
    r.raise_for_status()
    return r.json()