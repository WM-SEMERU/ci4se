def start(self):
    resp = self.post('start')
    if resp.is_fail():
        return None
    if 'result' not in resp.data:
        return None
    result = resp.data['result']
    return {'user': result['user'], 'ws_host': result['ws_host']}