def list(self, page=None, per_page=None, order_by='created_at', order_dir=
    'DESC', service='facebook'):
    params = {}
    if page:
        params['page'] = page
    if per_page:
        params['per_page'] = per_page
    if order_by:
        params['order_by'] = order_by
    if order_dir:
        params['order_dir'] = order_dir
    return self.request.get(service + '/get', params)