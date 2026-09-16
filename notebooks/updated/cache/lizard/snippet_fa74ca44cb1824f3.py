def cli(env, account_id):
    manager = SoftLayer.CDNManager(env.client)
    origins = manager.get_origins(account_id)
    table = formatting.Table(['id', 'media_type', 'cname', 'origin_url'])
    for origin in origins:
        table.add_row([origin['id'], origin['mediaType'], origin.get(
            'cname', formatting.blank()), origin['originUrl']])
    env.fout(table)