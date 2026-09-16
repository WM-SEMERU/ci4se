def get_schedule(self, ehr_username, start_date, changed_since, include_pix,
    other_user='All', end_date='', appointment_types=None, status_filter='All'
    ):
    if not start_date:
        raise ValueError('start_date can not be null')
    if end_date:
        start_date = '%s|%s' % (start_date, end_date)
    if not changed_since:
        changed_since = ''
    magic = self._magic_json(action=TouchWorksMagicConstants.
        ACTION_GET_SCHEDULE, app_name=self._app_name, user_id=ehr_username,
        token=self._token.token, parameter1=start_date, parameter2=
        changed_since, parameter3=include_pix, parameter4=other_user,
        parameter5=appointment_types, parameter6=status_filter)
    response = self._http_request(TouchWorksEndPoints.MAGIC_JSON, data=magic)
    result = self._get_results_or_raise_if_magic_invalid(magic, response,
        TouchWorksMagicConstants.RESULT_GET_SCHEDULE)
    return result