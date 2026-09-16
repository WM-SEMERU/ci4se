def get(self, id):
    ctx = self.context.copy()
    ctx['active_test'] = False
    results = self.rpc_model.search_read([('id', '=', id)], None, None,
        None, self.fields, context=ctx)
    return results and results[0] or None