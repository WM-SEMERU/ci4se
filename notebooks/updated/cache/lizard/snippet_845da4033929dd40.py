def compactor(conf):
    db = conf.get_database('compactor')
    limit_map = LimitContainer(conf, db)
    config = conf['compactor']
    if get_int(config, 'max_updates', 0) <= 0:
        LOG.warning(
            "Compaction is not enabled.  Enable it by setting a positive integer value for 'compactor.max_updates' in the configuration."
            )
    key_getter = GetBucketKey.factory(config, db)
    LOG.info('Compactor initialized')
    while True:
        try:
            buck_key = limits.BucketKey.decode(key_getter())
        except ValueError as exc:
            LOG.warning('Error interpreting bucket key: %s' % exc)
            continue
        if buck_key.version < 2:
            continue
        try:
            limit = limit_map[buck_key.uuid]
        except KeyError:
            LOG.warning('Unable to compact bucket for limit %s' % buck_key.uuid
                )
            continue
        LOG.debug('Compacting bucket %s' % buck_key)
        try:
            compact_bucket(db, buck_key, limit)
        except Exception:
            LOG.exception('Failed to compact bucket %s' % buck_key)
        else:
            LOG.debug('Finished compacting bucket %s' % buck_key)