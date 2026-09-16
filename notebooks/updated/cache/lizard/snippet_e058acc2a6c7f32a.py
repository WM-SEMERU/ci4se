def remove_filter(self, server_id, filter_path):
    server = self._get_server(server_id)
    conn_id = server.conn.conn_id if server.conn is not None else None
    ref_paths = server.conn.ReferenceNames(filter_path, ResultClass=
        SUBSCRIPTION_CLASSNAME)
    if ref_paths:
        raise CIMError(CIM_ERR_FAILED,
            'The indication filter is referenced by subscriptions.',
            conn_id=conn_id)
    server.conn.DeleteInstance(filter_path)
    inst_list = self._owned_filters[server_id]
    for i in six.moves.range(len(inst_list) - 1, -1, -1):
        inst = inst_list[i]
        if inst.path == filter_path:
            del inst_list[i]