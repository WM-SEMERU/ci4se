def rpc_get_namespace_cost(self, namespace_id, **con_info):
    if not check_namespace(namespace_id):
        return {'error': 'Invalid namespace', 'http_status': 400}
    db = get_db_state(self.working_dir)
    res = get_namespace_cost(db, namespace_id)
    db.close()
    units = res['units']
    amount = res['amount']
    ns = res['namespace']
    if amount is None:
        return {'error': 'Invalid namespace', 'http_status': 404}
    ret = {'units': units, 'amount': amount}
    if ns is not None:
        ret['warning'] = 'Namespace already exists'
    return self.success_response(ret)