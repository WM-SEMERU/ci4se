def view_cleanup(self):
    url = '/'.join((self.database_url, '_view_cleanup'))
    resp = self.r_session.post(url, headers={'Content-Type':
        'application/json'})
    resp.raise_for_status()
    return response_to_json_dict(resp)