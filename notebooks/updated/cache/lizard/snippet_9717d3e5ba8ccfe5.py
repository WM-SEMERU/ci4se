def _send_solr_command(self, core_url, json_command):
    url = _get_url(core_url, 'update')
    try:
        response = self.req_session.post(url, data=json_command, headers={
            'Content-Type': 'application/json'})
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error('Failed to send update to Solr endpoint [%s]: %s',
            core_url, e, exc_info=True)
        raise SolrException('Failed to send command to Solr [%s]: %s' % (
            core_url, e))
    return True