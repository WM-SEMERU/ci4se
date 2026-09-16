def _request_get(self, path, params=None, json=True, url=BASE_URL):
    url = urljoin(url, path)
    headers = self._get_request_headers()
    response = requests.get(url, params=params, headers=headers)
    if response.status_code >= 500:
        backoff = self._initial_backoff
        for _ in range(self._max_retries):
            time.sleep(backoff)
            backoff_response = requests.get(url, params=params, headers=
                headers, timeout=DEFAULT_TIMEOUT)
            if backoff_response.status_code < 500:
                response = backoff_response
                break
            backoff *= 2
    response.raise_for_status()
    if json:
        return response.json()
    else:
        return response