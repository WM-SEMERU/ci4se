def report(self, item_id, report_format='json'):
    report_format = report_format.lower()
    response = self._request('/report/{job_id}/summary'.format(job_id=item_id))
    if response.status_code == 429:
        raise sandboxapi.SandboxError(
            'API rate limit exceeded while fetching report')
    if report_format == 'json':
        try:
            return json.loads(response.content.decode('utf-8'))
        except ValueError:
            pass
    return response.content.decode('utf-8')