def cli(env, sortby):
    manager = SoftLayer.CDNManager(env.client)
    accounts = manager.list_accounts()
    table = formatting.Table(['id', 'account_name', 'type', 'created', 'notes']
        )
    for account in accounts:
        table.add_row([account['id'], account['cdnAccountName'], account[
            'cdnSolutionName'], account['createDate'], account.get(
            'cdnAccountNote', formatting.blank())])
    table.sortby = sortby
    env.fout(table)