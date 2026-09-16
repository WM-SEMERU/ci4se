def cli(env, name, description):
    mgr = SoftLayer.NetworkManager(env.client)
    result = mgr.create_securitygroup(name, description)
    table = formatting.KeyValueTable(['name', 'value'])
    table.align['name'] = 'r'
    table.align['value'] = 'l'
    table.add_row(['id', result['id']])
    table.add_row(['name', result.get('name') or formatting.blank()])
    table.add_row(['description', result.get('description') or formatting.
        blank()])
    table.add_row(['created', result['createDate']])
    env.fout(table)