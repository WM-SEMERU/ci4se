def cli(env, identifier):
    mgr = SoftLayer.DedicatedHostManager(env.client)
    host_id = helpers.resolve_id(mgr.resolve_ids, identifier, 'dedicated host')
    if not (env.skip_confirmations or formatting.no_going_back(host_id)):
        raise exceptions.CLIAbort('Aborted')
    mgr.cancel_host(host_id)
    click.secho('Dedicated Host %s was cancelled' % host_id, fg='green')