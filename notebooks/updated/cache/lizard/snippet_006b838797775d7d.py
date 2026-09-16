def cli(env, identifier):
    dh_mgr = SoftLayer.DedicatedHostManager(env.client)
    host_id = helpers.resolve_id(dh_mgr.resolve_ids, identifier,
        'dedicated host')
    if not (env.skip_confirmations or formatting.no_going_back(host_id)):
        raise exceptions.CLIAbort('Aborted')
    table = formatting.Table(['id', 'server name', 'status'])
    result = dh_mgr.cancel_guests(host_id)
    if result:
        for status in result:
            table.add_row([status['id'], status['fqdn'], status['status']])
        env.fout(table)
    else:
        click.secho('There is not any guest into the dedicated host %s' %
            host_id, fg='red')