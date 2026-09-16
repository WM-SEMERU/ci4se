def _get_handler(self, node_id):
    handler = self._get_attrs(node_id).get(self.HANDLER, self._default_handler)
    if not isinstance(handler, BasicNodeHandler):
        idaapi.msg(
            'Invalid handler for node {}: {}. All handlers must inherit from`BasicNodeHandler`.'
            .format(node_id, handler))
        handler = self._default_handler
    return handler