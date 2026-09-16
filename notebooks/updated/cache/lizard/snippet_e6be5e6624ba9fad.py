def _create_snapshot(volume):
    logger.info('Creating new snapshot for {}'.format(volume.id))
    snapshot = volume.create_snapshot(description=
        'Automatic snapshot by Automated EBS Snapshots')
    logger.info('Created snapshot {} for volume {}'.format(snapshot.id,
        volume.id))
    return snapshot