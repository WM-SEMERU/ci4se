def _config_profile_list(self):
    url = self._cfg_profile_list_url
    payload = {}
    try:
        res = self._send_request('GET', url, payload, 'config-profile')
        if res and res.status_code in self._resp_ok:
            return res.json()
    except dexc.DfaClientRequestFailed:
        LOG.error('Failed to send request to DCNM.')