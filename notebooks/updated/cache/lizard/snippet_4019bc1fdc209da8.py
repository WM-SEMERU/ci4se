def user_activity_stats_by_date(self, username, date, grouped=None):
    request_url = '{}/api/0/user/{}/activity/{}'.format(self.instance,
        username, date)
    payload = {}
    if username is not None:
        payload['username'] = username
    if date is not None:
        payload['date'] = date
    if grouped is not None:
        payload['grouped'] = grouped
    return_value = self._call_api(request_url, params=payload)
    return return_value['activities']