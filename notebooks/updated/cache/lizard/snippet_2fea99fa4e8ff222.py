def client_get(self, url, **kwargs):
    response = requests.get(self.make_url(url), headers=self.headers)
    if not response.ok:
        raise Exception('{status}: {reason}.\nCircleCI Status NOT OK'.
            format(status=response.status_code, reason=response.reason))
    return response.json()