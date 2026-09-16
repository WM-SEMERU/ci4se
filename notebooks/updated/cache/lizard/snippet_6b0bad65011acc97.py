def report_verifications(self, start_date, end_date):
    start_str, end_str = self._format_input_dates(start_date, end_date)
    params = {'start_date': start_str, 'end_date': end_str}
    response = self._get(url.reports_verifications, params=params)
    self._check_response(response, 200)
    return self._create_response(response)