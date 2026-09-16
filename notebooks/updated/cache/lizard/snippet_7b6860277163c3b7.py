def get_os_and_browsers(self):
    resp = self.session.get(os.path.join(self.api_url, 'browsers.json'))
    resp = self._process_response(resp)
    return resp.json()