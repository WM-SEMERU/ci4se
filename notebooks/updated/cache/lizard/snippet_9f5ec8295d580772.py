def cli(env, volume_id, reason, immediate):
    file_storage_manager = SoftLayer.FileStorageManager(env.client)
    if not (env.skip_confirmations or formatting.no_going_back(volume_id)):
        raise exceptions.CLIAbort('Aborted')
    cancelled = file_storage_manager.cancel_snapshot_space(volume_id,
        reason, immediate)
    if cancelled:
        if immediate:
            click.echo(
                'File volume with id %s has been marked for immediate snapshot cancellation'
                 % volume_id)
        else:
            click.echo(
                'File volume with id %s has been marked for snapshot cancellation'
                 % volume_id)
    else:
        click.echo('Unable to cancel snapshot space for file volume %s' %
            volume_id)