def cli(env, volume_id, replicant_id):
    block_storage_manager = SoftLayer.BlockStorageManager(env.client)
    success = block_storage_manager.failback_from_replicant(volume_id,
        replicant_id)
    if success:
        click.echo('Failback from replicant is now in progress.')
    else:
        click.echo('Failback operation could not be initiated.')