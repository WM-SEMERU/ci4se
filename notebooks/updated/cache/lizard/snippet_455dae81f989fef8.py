def delete_doc_by_query(self, collection, query, **kwargs):
    temp = {'delete': {'query': query}}
    resp, con_inf = self.transport.send_request(method='POST', endpoint=
        'update', collection=collection, data=json.dumps(temp), **kwargs)
    return resp