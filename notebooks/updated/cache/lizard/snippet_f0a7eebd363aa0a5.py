def get_diagnosis(self, remediation_id=None):
    diag_url = (self.base_url + '/remediations/v1/diagnosis/' +
        generate_machine_id())
    params = {}
    if remediation_id:
        params['remediation'] = remediation_id
    try:
        net_logger.info('GET %s', diag_url)
        res = self.session.get(diag_url, params=params, timeout=self.config
            .http_timeout)
    except (requests.ConnectionError, requests.Timeout) as e:
        logger.error(e)
        logger.error('The Insights API could not be reached.')
        return False
    if self.handle_fail_rcs(res):
        logger.error('Unable to get diagnosis data: %s %s', res.status_code,
            res.text)
        return None
    return res.json()