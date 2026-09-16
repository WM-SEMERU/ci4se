def _patch(self, uri, data):
    headers = self._get_headers()
    response = self.session.patch(uri, headers=headers, data=json.dumps(data))
    if response.status_code == 204:
        return response
    else:
        logging.error(response.content)
        response.raise_for_status()