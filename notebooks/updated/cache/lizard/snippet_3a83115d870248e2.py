def delete(self, synchronous=True):
    response = self.delete_raw()
    response.raise_for_status()
    if synchronous is True and response.status_code == http_client.ACCEPTED:
        return _poll_task(response.json()['id'], self._server_config)
    elif response.status_code == http_client.NO_CONTENT or response.status_code == http_client.OK and hasattr(
        response, 'content') and not response.content.strip():
        return
    return response.json()