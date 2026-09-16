def cli(env):
    manager = SoftLayer.IPSECManager(env.client)
    contexts = manager.get_tunnel_contexts()
    table = formatting.Table(['id', 'name', 'friendly name',
        'internal peer IP address', 'remote peer IP address', 'created'])
    for context in contexts:
        table.add_row([context.get('id', ''), context.get('name', ''),
            context.get('friendlyName', ''), context.get(
            'internalPeerIpAddress', ''), context.get(
            'customerPeerIpAddress', ''), context.get('createDate', '')])
    env.fout(table)