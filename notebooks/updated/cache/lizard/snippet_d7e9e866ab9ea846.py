def cli(env, identifier, wait):
    compute = SoftLayer.HardwareManager(env.client)
    compute_id = helpers.resolve_id(compute.resolve_ids, identifier, 'hardware'
        )
    ready = compute.wait_for_ready(compute_id, wait)
    if ready:
        env.fout('READY')
    else:
        raise exceptions.CLIAbort('Server %s not ready' % compute_id)