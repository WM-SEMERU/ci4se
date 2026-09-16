def _fetch_system_by_machine_id(self):
    machine_id = generate_machine_id()
    try:
        url = self.api_url + '/inventory/v1/hosts?insights_id=' + machine_id
        net_logger.info('GET %s', url)
        res = self.session.get(url, timeout=self.config.http_timeout)
    except (requests.ConnectionError, requests.Timeout) as e:
        logger.error(e)
        logger.error('The Insights API could not be reached.')
        return None
    try:
        if self.handle_fail_rcs(res):
            return None
        res_json = json.loads(res.content)
    except ValueError as e:
        logger.error(e)
        logger.error('Could not parse response body.')
        return None
    if res_json['total'] == 0:
        logger.debug('No hosts found with machine ID: %s', machine_id)
        return False
    return res_json['results']