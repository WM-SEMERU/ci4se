def is_running(self):
    try:
        result = requests.get(self.proxy_url)
    except RequestException:
        return False
    if 'ZAP-Header' in result.headers.get('Access-Control-Allow-Headers', []):
        return True
    raise ZAPError('Another process is listening on {0}'.format(self.proxy_url)
        )