def resume(env, identifier):
    vsi = SoftLayer.VSManager(env.client)
    vs_id = helpers.resolve_id(vsi.resolve_ids, identifier, 'VS')
    env.client['Virtual_Guest'].resume(id=vs_id)