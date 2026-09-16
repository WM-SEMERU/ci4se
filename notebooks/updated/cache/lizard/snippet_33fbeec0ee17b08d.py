def _create_destination(self, server_id, dest_url, owned):
    server = self._get_server(server_id)
    host, port, ssl = parse_url(dest_url, allow_defaults=False)
    schema = 'https' if ssl else 'http'
    listener_url = '{0}://{1}:{2}'.format(schema, host, port)
    this_host = getfqdn()
    ownership = 'owned' if owned else 'permanent'
    dest_path = CIMInstanceName(DESTINATION_CLASSNAME, namespace=server.
        interop_ns)
    dest_inst = CIMInstance(DESTINATION_CLASSNAME)
    dest_inst.path = dest_path
    dest_inst['CreationClassName'] = DESTINATION_CLASSNAME
    dest_inst['SystemCreationClassName'] = SYSTEM_CREATION_CLASSNAME
    dest_inst['SystemName'] = this_host
    dest_inst['Name'] = _format('pywbemdestination:{0}:{1}:{2}', ownership,
        self._subscription_manager_id, uuid.uuid4())
    dest_inst['Destination'] = listener_url
    if owned:
        for i, inst in enumerate(self._owned_destinations[server_id]):
            if inst.path == dest_path:
                if inst != dest_inst:
                    server.conn.ModifyInstance(dest_inst)
                    dest_inst = server.conn.GetInstance(dest_path)
                    self._owned_destinations[server_id][i] = dest_inst
                return dest_inst
        dest_path = server.conn.CreateInstance(dest_inst)
        dest_inst = server.conn.GetInstance(dest_path)
        self._owned_destinations[server_id].append(dest_inst)
    else:
        dest_path = server.conn.CreateInstance(dest_inst)
        dest_inst = server.conn.GetInstance(dest_path)
    return dest_inst