def delete_intel_notifications(self, ids, timeout=None):
    if not isinstance(ids, list):
        raise TypeError('ids must be a list')
    data = json.dumps(ids)
    try:
        response = requests.post(self.base +
            'hunting/delete-notifications/programmatic/?key=' + self.
            api_key, data=data, proxies=self.proxies, timeout=timeout)
    except requests.RequestException as e:
        return dict(error=str(e))
    return _return_response_and_status_code(response)