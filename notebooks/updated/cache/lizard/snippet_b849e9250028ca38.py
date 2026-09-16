def _get_provisioning_state(self, response):
    if self._is_empty(response):
        return None
    body = response.json()
    return body.get('properties', {}).get('provisioningState')