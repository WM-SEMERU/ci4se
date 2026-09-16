def batch(self, reqs):
    batch_data = []
    for req_id, req in enumerate(reqs):
        batch_data.append({'method': req[0], 'params': req[1], 'jsonrpc':
            '2.0', 'id': req_id})
    data = json.dumps(batch_data)
    response = self.session.post(self.url, data=data).json()
    return response